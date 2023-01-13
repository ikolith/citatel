import yaml
import re
import os
from pprint import pprint
from typing import Union
from random import randint

import citutils.dice_utils as du
import citutils.entity_text_generators as ge
import citutils.my_types as ty


def get_clean_name(name: str) -> str:
    """Returns a name in lowercase with numbers left alone, whitespace stripped, " " and "-" replaced with "_", and every other character removed."""
    return re.sub(
        r"[^a-z1-9_]", "", name.lower().strip().replace(" ", "_").replace("-", "_")
    )


def add_expanded_outcomes(entity: ty.Entity) -> ty.Entity:
    # TODO: remember its possible to roll above the max value of a table, at which point you should pick the max result... or that will be a configurable thing! id ont knwo
    # likely, rather than making this, i should be figuring out ranges when i need them and not preprocessing, though on the other hand this does make it a lot easier to just grab an outcome from any function without calling another one...
    expanded_outcomes = {}
    for outcome_k, outcome_v in entity["table"]["outcomes"].items():
        if (
            type(outcome_k) == str
            and (match_k := re.search(r"(\d*)-(\d*)", outcome_k)) is not None
        ):
            start, end = match_k.groups()
            for new_k in range(int(start), int(end) + 1):
                expanded_outcomes[int(new_k)] = outcome_v
        else:
            expanded_outcomes[int(outcome_k)] = outcome_v
    entity["table"]["expanded_outcomes"] = expanded_outcomes
    return entity


def get_entities(dir_path: str, sort: bool = False) -> ty.Entities:
    entities = ty.Entities({})
    entity_files = []
    for file in os.listdir(dir_path):
        if file.endswith(".yaml"):
            entity_files.append(os.path.join(dir_path, file))
    for file in entity_files:
        with open(file, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if data is None:
                continue
            for entity in data:
                # up to here is same as in standard
                if "table" in entity.keys():
                    entity = add_expanded_outcomes(entity)
                for k, v in entity.items():
                    if k != "table":  # surely this is not the best way to do this...
                        entity[k] = str(v)
                clean_name = get_clean_name(entity["name"])
                assert not clean_name in entities
                entities[clean_name] = entity
    if sort:
        entities = dict(sorted(entities.items()))
    return entities


def parse_curlies(text: str) -> list[ty.Curly]:
    curlies = re.findall(r"{[^}]*}", text)
    dice_pattern = r"\d*?d\d+x?[+-]?\d*"
    # good chance there will be a change in how die parsing works
    # and this pattern is used multiple places, this should make it easier to track/change...
    curlies_parsed = []
    if curlies:
        for match in curlies:
            # Check for entity...
            quantity = 1
            if (e := re.search(r"(?<=\s|{)([a-zA-Z_\s]+)", match)) is not None:
                entity = get_clean_name(e.group())
            else:
                entity = ""
            # Check for quantity dice (leading dice)...
            if q := re.search(rf"(?<={{){dice_pattern}", match):
                quantity_dice = q.group()
                quantity = du.die_parser_roller(quantity_dice)
            # Check for number
            else:
                if entity == "":
                    break
                elif (n := re.search(r"(?<={)\d+(?=\s)", match)) is not None:
                    quantity_dice = ""
                    quantity = int(n.group())
                else:
                    quantity_dice = ""
            if entity and (t := re.search(rf"({dice_pattern})(?=}})", match)):
                table_dice = t.group()
                table_result = du.die_parser_roller(table_dice)
            else:
                table_dice = ""
                table_result = None
            curlies_parsed.append(
                ty.Curly(
                    {
                        "match": match,
                        "quantity_dice": quantity_dice,
                        "table_dice": table_dice,
                        "entity": entity,
                        "quantity": quantity,
                        "table_result": table_result,
                    }
                )
            )
    return curlies_parsed


def roll_on_table(
    entities: ty.Entities, curly: ty.Curly, bound_roll: bool = True
) -> str:
    # bound_roll means that if the roll is lower than min, it becomes min, if it is higher than max, it becomes max
    table = entities[curly["entity"]]["table"]
    roll_min = int(min(table["expanded_outcomes"].keys()))
    roll_max = int(max(table["expanded_outcomes"].keys()))
    if curly["table_dice"]:
        roll = curly["table_result"]
    elif "roll" in table.keys():
        roll = du.die_parser_roller((table["roll"]))
    else:
        roll = randint(
            roll_min,
            roll_max,
        )
    if bound_roll:
        if roll > roll_max:
            roll = roll_max
        elif roll < roll_min:
            roll = roll_min
    # doesnt seem like the preprocess buys as much as i thought it might!
    return table["expanded_outcomes"][roll]


def get_replacement_text(
    base_text: str,
    curlies_parsed: list,
) -> str:
    # roll_results = [curly["quantity"] for curly in curlies_parsed]
    # if not roll_results:
    #     roll_results = [match["quantity_roll"] for match in curlies_parsed]
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


def text_is_unique(
    text: str,
) -> bool:  # TODO: remove this if it didnt come back into the main func
    return any([curly["quantity_dice"] for curly in parse_curlies(text)])


def text_has_children(text: str) -> bool:
    return any([curly["entity"] for curly in parse_curlies(text)])


# entity tree functions


def generate_entity_tree_and_non_unique(
    entities: ty.Entities,
    base_curly: ty.Curly,
    expand_entities: bool = False,
    roll_dice: bool = False,
    html_characters: bool = False,
) -> tuple[ty.EntityTree, ty.NonUniqueEntities]:
    non_unique_entities = ty.NonUniqueEntities({})
    entity_tree = ty.EntityTree([])
    curly_queue = [[base_curly] * base_curly["quantity"]]
    while len(curly_queue) != 0 and len(entity_tree) < 100:
        # TODO: looking back up the tree to not recurse
        curlies = curly_queue.pop(0)
        parent_id = len(entity_tree) - 1
        for curly in curlies:  # note that this single element is a list of curlies
            # skips case where the curly is just a roll.
            if not curly["entity"]:
                continue
            # uniqueness testing
            has_table = "table" in entities[curly["entity"]].keys()  # TODO: not tested
            entity_text = ge.generate_entity_text(
                entities[curly["entity"]],
                text_type="md",
                html_characters=html_characters,
                skip_table=roll_dice,
                # if we are rolling dice, then we dont want the whole table, instead we just handle the result of the table!
            )
            if roll_dice:  # now we handle that table we skipped!
                entity_text += (
                    f"Table Result:  \n" + roll_on_table(entities, curly) + "\n"
                )
            curlies_parsed = parse_curlies(entity_text)
            if any(
                [inner_curly["quantity_dice"] for inner_curly in curlies_parsed]
            ) or (has_table and roll_dice):
                unique = True
            else:
                unique = False
                # this uniqueness detection is not perfect!
                # two entities could end up rolling the same dice and/or have the same table result, so they would be identical, but both counted as "unique"
                # "uniqueness" here is an anticipation of inherent randomness/randomization, its not a guarantee of not-being-identical!
                # maybe it should be! but it is not for either dice rolling or table rolling, and im fine with that for now.
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
                ty.TreeEntry(
                    {
                        "id": len(entity_tree),
                        "entity": curly["entity"],
                        "children": [],
                        "unique": unique,
                        "text": entity_text,
                        "curly": curly,
                    }
                )
            )
    return entity_tree, non_unique_entities


# TODO: possible the answer is here..
def generate_entity_tree_text(
    entities: ty.Entities,
    base_curly: ty.Curly,
    expand_entities: bool = False,
    roll_dice: bool = False,
    html_characters: bool = False,
) -> str:
    base_quantity = base_curly["quantity"]
    # just need this line for the fancy name:
    base_entity = entities[base_curly["entity"]]
    base_entity_text = ge.generate_entity_text(
        entities[base_curly["entity"]], html_characters=html_characters
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
        entities, base_curly, expand_entities, roll_dice
    )
    if not len(non_unique_entities) == 0:
        non_unique_text = """### Non Unique Entities:\n"""
        for clean_name, v in non_unique_entities.items():
            non_unique_text += f"\n{v['count']} {clean_name}  \n\n{v['text']}"
    else:
        non_unique_text = ""
    entity_text = """\n### Unique Entities, Full Tree:\n"""
    for n in entity_tree:
        if n["unique"]:
            entity_text += "\n" + n["text"]
    return (non_unique_text + entity_text).strip()


# misc. parsers


def single_curly_parser(
    text: str,
    entities: ty.Entities,
    expand_entities: bool = False,
    roll_dice: bool = False,
) -> str:
    if not (text.startswith("{") and text.endswith("}")):
        text = "{" + text + "}"
    curlies_parsed = parse_curlies(text)
    assert len(curlies_parsed) == 1
    base_curly = curlies_parsed[0]
    # case when only die roll is present
    if not base_curly["entity"]:
        return str(du.die_parser_roller(base_curly["quantity_result"]))
    # all other cases
    return generate_entity_tree_text(entities, base_curly, expand_entities, roll_dice)
