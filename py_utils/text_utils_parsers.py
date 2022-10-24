import yaml
import py_utils.dice_utils as d
import py_utils.entity_text_generators as g
from pprint import pprint
import re
import os
import logging  # TODO: add logging


def get_clean_name(name: str) -> str:
    """Returns a name in lowercase with numbers left alone, whitespace stripped, " " and "-" replaced with "_", and every other character removed."""
    return re.sub(
        r"[^a-z1-9_]", "", name.lower().strip().replace(" ", "_").replace("-", "_")
    )


def get_entities(dir_path: str) -> dict[dict]:
    entities = {}
    entity_files = []
    for file in os.listdir(dir_path):
        if file.endswith(".yaml"):
            entity_files.append(os.path.join(dir_path, file))
    for file in entity_files:
        with open(file) as f:
            data = yaml.safe_load(f)
            for entity in data:
                for k, v in entity.items():
                    entity[k] = str(v)
                clean_name = get_clean_name(entity["name"])
                assert not clean_name in entities
                entities[clean_name] = entity
    return entities


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
                    quantity = int(n.group())
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


def text_is_unique(text: str) -> bool:
    return any([curly["roll"] for curly in parse_curlies(text)])


def text_has_children(text: str) -> bool:
    return any([curly["entity"] for curly in parse_curlies(text)])


# entity tree functions


def generate_entity_tree_and_non_unique(
    base_curly: dict,
    entities: dict[str, dict[str, str]],
    expand_entities: bool = False,
    roll_dice: bool = False,
    html_characters: bool = False,
    text_type: str = "md",
) -> tuple[
    list, dict
]:  # this typing could be more verbose.. but really we just need curlies to be a NewType
    non_unique_entities = {}
    entity_tree = []
    curly_queue = [[base_curly] * base_curly["quantity"]]
    while len(curly_queue) != 0 and len(entity_tree) < 100:
        # TODO: looking back up the tree to not recurse
        curlies = curly_queue.pop(0)
        parent_id = len(entity_tree) - 1
        for curly in curlies:  # note that this single element is a list of curlies
            # skips case where the curly is just a roll.
            if not curly["entity"]:
                continue
            entity_text = g.generate_entity_text(
                entities[curly["entity"]], text_type, html_characters
            )
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
                    if not curly["entity"] or curly["quantity"] == 0:
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
    entities: dict[str, dict[str, str]],
    expand_entities: bool = False,
    roll_dice: bool = False,
    html_characters: bool = False,
    text_type: str = "md",
) -> str:
    base_quantity = base_curly["quantity"]
    # just need this line for the fancy name:
    base_entity = entities[base_curly["entity"]]
    base_entity_text = g.generate_entity_text(
        entities[base_curly["entity"]], text_type, html_characters
    )
    if not expand_entities or not text_has_children(base_entity_text):
        if roll_dice:
            n_base_entity = str(base_quantity) + " " + base_entity["name"] + "\n"
            curlies_parsed = parse_curlies(base_entity_text)
            return n_base_entity + get_replacement_text(
                base_text=base_entity_text, curlies_parsed=curlies_parsed
            )
        else:
            return base_entity_text
    entity_tree, non_unique_entities = generate_entity_tree_and_non_unique(
        base_curly, entities, expand_entities, roll_dice
    )

    non_unique_text = """--------\nNon Unique Entities:\n--------"""
    entity_text = """\n--------\nUnique Entities, Full Tree:\n--------"""

    for clean_name, v in non_unique_entities.items():
        non_unique_text += f"\n{v['count']} {clean_name}\n{v['text']}"
    for n in entity_tree:
        if n["unique"]:
            entity_text += "\n" + n["text"]
    return non_unique_text + entity_text
