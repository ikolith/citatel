from typing import NewType
import pandas as pd
import py_utils.dice_utils as d
import py_utils.entity_text_generators as g
import pprint
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


def parse_curlies(text: str) -> list[dict[str, str, str, int]]:
    curlies = re.findall(r"{[^}]*}", text)
    curlies_parsed = []
    if curlies:
        for match in curlies:
            # Check for entity...
            quantity = 1
            if (e := re.search(r"(?<=\s|{)([a-z_]*)(?=})", match)) is not None:
                entity = e.group()
            else:
                entity = ""
            # Check for dice...
            if r := re.search(r"(?<={)\d*?d\d+x?[+-]?\d*", match):
                roll = r.group()
                quantity = d.die_parser_roller(roll)
            # Check for number
            else:
                if entity == "":
                    break
                elif (n := re.search(r"(?<={)\d+(?=\s)", match)) is not None:
                    roll = ""
                    quantity = n.group()
                else:
                    roll = ""
            curlies_parsed.append(
                {
                    "match": match,
                    "roll": roll,
                    "entity": entity,
                    "quantity": quantity,
                }
            )
    return curlies_parsed


def get_replacement_text(
    base_text: str,
    curlies_parsed: list,
) -> str:
    # roll_results = [curly["quantity"] for curly in curlies_parsed]
    # if not roll_results:
    #     roll_results = [match["roll"] for match in curlies_parsed]
    for i, curly_match in enumerate(curlies_parsed):
        if curly_match["quantity"] == 0:
            base_text = base_text.replace(curly_match["match"], "", 1)
        else:
            base_text = base_text.replace(
                curly_match["match"],
                f"""{curly_match['quantity']} {curly_match['entity']}""".strip(),
                1,
            )
    return base_text


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
    non_unique_entities = {}
    entity_tree = []
    curly_queue = [[base_curly]]
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
            if roll_dice:
                curlies_parsed = parse_curlies(entity_text)
                entity_text = get_replacement_text(
                    base_text=entity_text, curlies_parsed=curlies_parsed
                )
                for curly in curlies_parsed:
                    if not curly["entity"]:
                        pass
                    else:
                        curly_queue += [[curly] * curly["quantity"]]
            else:
                curly_queue.append(parse_curlies(entity_text))
            if parent_id >= 0:
                entity_tree[parent_id]["children"].append(len(entity_tree) - 1)
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
    return entity_tree, non_unique_entities


def generate_entity_tree_text(
    base_curly: dict,
    all_data: dict,
    expand_entities=False,
    roll_dice=False,
    text_type="plaintext",
) -> str:
    base_quantity = base_curly["quantity"]
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
                base_text=base_text, curlies_parsed=curlies_parsed
            )
        else:
            return base_text
    entity_tree, non_unique_entities = generate_entity_tree_and_non_unique(
        base_curly, all_data, expand_entities, roll_dice
    )
    non_unique_text = """--------\nNon Unique Entities:\n--------"""
    entity_text = """\n--------\nUnique Entities, Full Tree:\n--------"""

    for clean_name, v in non_unique_entities.items():
        non_unique_text += f"\n{v['count']} {clean_name}\n{v['text']}"
    for n in entity_tree:
        if n["unique"]:
            entity_text += "\n" + n["text"]
    return non_unique_text + entity_text
