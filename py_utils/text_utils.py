from typing import NewType
import pandas as pd
import py_utils.dice_utils as d
import py_utils.entity_text_generators as g
import re
import os

# loading csvs, cleaning_csvs, building all_data


def load(path: str) -> pd.DataFrame:
    return pd.read_csv(path, header=0).dropna(subset="name").fillna("")


def clean_name(name: list) -> list:
    """Returns a name in lowercase with whitespace stripped, " " and "-" replaced with "_" and every other chatacter removed."""
    return re.sub(
        r"[^a-z1-9_]", "", name.lower().strip().replace(" ", "_").replace("-", "_")
    )


def csv_add_clean_name(path: str) -> None:
    df = load(path)
    df["clean_name"] = df["name"].apply(clean_name)
    df.to_csv(path, index=False)


def get_all_data(
    armors="", invocations="", items="", npcs="", weapons="", skills=""
) -> dict:
    """This function wants paths to csvs.
    It returns a dictionary with the the type of entity as key and a DataFrame of all the relevant csvs values."""
    paths = {
        "armors": armors,
        "invocations": invocations,
        "items": items,
        "npcs": npcs,
        "weapons": weapons,
        "skills": skills,
    }
    all_data = {}
    for entity, path in paths.items():
        if path:
            csv_add_clean_name(path)
            all_data[entity] = load(path)
            all_data[entity]["filter_tags"] = all_data[entity]["filter_tags"].map(
                lambda x: x.replace(" ", "").split(sep=",")
            )
    return all_data


def parse_curlies(text: str) -> list[dict[str, str, str]]:
    curlies = re.findall(r"{[^}]*}", text)
    curlies_parsed = []
    if curlies:
        for match in curlies:
            # Check for entity...
            if (e := re.search(r"(?<=\s|{)([a-z_]*)(?=})", match)) is not None:
                entity = e.group()
            else:
                entity = ""
            # Check for dice...
            if r := re.search(r"(?<={)\d*?d\d+x?[+-]?\d*", match):
                roll = r.group()
            # Check for number
            else:
                if entity == "":
                    break
                elif (n := re.search(r"(?<={)\d+(?=\s)", match)) is not None:
                    roll = n.group()
                else:
                    roll = ""
            curlies_parsed.append({"match": match, "roll": roll, "entity": entity})
    return curlies_parsed


def get_replacement_text(
    text: str,
    curlies_parsed: list,
    roll_results: list = [],
) -> str:
    if not roll_results:
        roll_results = [match["roll"] for match in curlies_parsed]
    for i, curly_match in enumerate(curlies_parsed):
        if roll_results[i] == 0:
            text = text.replace(curly_match["match"], "", 1)
        else:
            text = text.replace(
                curly_match["match"],
                f"{roll_results[i]} {curly_match['entity']}".strip(),
                1,
            )
    return text


def search_all_data(clean_name: str, all_data: dict) -> tuple[str, pd.Series]:
    for entity_type, data in all_data.items():
        if clean_name in data.clean_name.values:
            return entity_type, data.loc[data["clean_name"] == clean_name].squeeze()
            # TODO: this sucks. search_all_data was built to return one series, one row. increasingly there are cases where we want many rows, and calling this many times is pretty suboptimal. neither this function nor any of the functions that rely on it can handle many rows. This should return a dataframe and take as input a list of clean_names.. probably. also generate_entity_tree(_text) or whatever should cache more. optimizations needed.
    raise Exception(f"Couldn't find {clean_name} in all_data")


def text_is_unique(text: str) -> bool:
    return any([curly["roll"] for curly in parse_curlies(text)])


def text_has_children(text: str) -> bool:
    return any([curly["entity"] for curly in parse_curlies(text)])


def search_for_text(
    clean_name: str, all_data: dict, text_type: str = "plaintext"
) -> str:
    return g.generate_entity_text(*search_all_data(clean_name, all_data), text_type)


# entity tree functions


def generate_entity_tree_and_non_unique(
    base_curly: dict,
    all_data: dict,
    expand_entities=False,
    roll_dice=False,
    text_type="plaintext",
) -> tuple[
    list, dict
]:  # this typing could be more verbose.. but really we just need curlies to be a NewType
    # TODO: idea at some point to move base case into while though now im not so sure that this is necessary or good...i will probably just not do it yet and do the more pressing stuff first
    non_unique_entities = {}
    base_text = search_for_text(base_curly["entity"], all_data, text_type)
    entity_tree = [
        {
            "entity": base_curly["entity"],
            "unique": True,
            "text": base_text,
            "children": [],
        }
    ]  # the index here is equivalent to an id,
    # the index will be how parents/children will be assigned later
    if not text_is_unique(base_text):
        non_unique_entities[base_curly["entity"]] = {"text": base_text, "count": 1}
    curly_queue = [parse_curlies(base_text)]
    while len(curly_queue) != 0 and len(entity_tree) < 100:
        # TODO: looking back up the tree to not recurse
        curlies = curly_queue.pop(0)
        parent_id = len(entity_tree) - 1
        for curly in curlies:  # note that this single element is a list of curlies
            # skips case where the curly is just a roll.
            if not curly["entity"]:
                continue

            entity_text = search_for_text(curly["entity"], all_data, text_type)
            unique = text_is_unique(entity_text)

            # deals with case where this is not unique...
            if not unique:
                # ... and we have seen it before:
                if curly["entity"] in non_unique_entities.keys():
                    non_unique_entities[curly["entity"]]["count"] += 1
                # ... and we haven't seen it before:
                else:
                    non_unique_entities[curly["entity"]] = {
                        "text": entity_text,
                        "count": 1,
                    }
                entity_text = ""
            entity_tree.append(
                {
                    "id": len(entity_tree),
                    "entity": curly["entity"],
                    "children": [],
                    "unique": unique,
                    "text": entity_text,
                    "curly": curly,
                }
            )
            entity_tree[parent_id]["children"].append(len(entity_tree) - 1)
            curly_queue.append(parse_curlies(entity_text))
    return entity_tree, non_unique_entities


def generate_entity_tree_text(
    base_curly: dict,
    all_data: dict,
    expand_entities=False,
    roll_dice=False,
    text_type="plaintext",
) -> str:

    base_quantity = d.die_parser_roller(base_curly["roll"]) if base_curly["roll"] else 1
    # just need this line for the fancy name:
    _, base_row = search_all_data(base_curly["entity"], all_data)
    base_text = search_for_text(
        base_curly["entity"], all_data, text_type
    )  # this just means calling text twice... eh
    if not expand_entities or not text_has_children(base_text):
        if roll_dice:
            n_base_entity = str(base_quantity) + " " + base_row["name"] + "\n"
            curlies_parsed = parse_curlies(base_text)
            return n_base_entity + get_replacement_text(
                text=base_text, curlies_parsed=curlies_parsed
            )
        else:
            return base_text
    # at this point we guarantee that the base case entity has children, though we are uncertain on rolling
    entity_tree, non_unique_entities = generate_entity_tree_and_non_unique(
        base_curly, all_data, expand_entities, roll_dice
    )
    # should a given unique include a list of non_unique entities it has??
    non_unique_text = """--------\nNon Unique Entities:\n--------"""
    entity_text = """\n--------\nUnique Entities, Full Tree:\n--------"""
    if not roll_dice:
        for clean_name, v in non_unique_entities.items():
            non_unique_text += f"\n{v['count']} {clean_name}\n{v['text']}"
        for n in entity_tree:
            text = n["text"] if n["unique"] else g.name_plaintext(n["entity"])
            entity_text += str("\n" + text)
        return non_unique_text + entity_text
    # roll dice and expand
    print(entity_tree)
    for n in entity_tree:
        # TODO: roll-expand
        pass
    # now have to deal with traversing the tree and Not rolling dice
