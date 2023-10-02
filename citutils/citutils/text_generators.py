import os
from copy import deepcopy
import re

import citutils.parsers as p
import citutils.my_types as ty
import citutils.database as dt
import citutils.dice_utils as du
import citutils.text_formatters as tf

# single entity text generators. used for cli and various utilities.


def generate_latex(
    entity: dict,
    formatting: dict[str, dict] = tf.formatting_dict_latex,
    footer: bool = True,
) -> str:
    result_text = ""
    for k, v in entity.items():
        result_text += tf.if_exists_format_latex(text=v, **tf.formatting_dict_latex[k])
    if footer and "encumbrance" in entity.keys():
        result_text += rf"""\vfill
        \hfill {"Enc: " + entity["encumbrance"]} 
        """
    return result_text


def generate_md(
    entity: dict,
    formatting: dict = tf.formatting_dict_md,
) -> str:
    result_text = ""
    for key, text in entity.items():
        result_text += tf.if_exists_format_md(text=text, **formatting[key])
    return result_text


def prep_latex(entity_local: ty.Entity) -> str | list:
    funcs = [
        # removes curlies as they shouldn't show up in latex. they'd have to be escaped for  tex anyhow
        (lambda v: re.sub(r"[{}]", "", v)),
        # escape "_" which will otherwise break the tex
        (lambda v: re.sub(r"([a-z0-9])(_)", r"\1\_", v)),
        # a nicer arrow :)
        (lambda v: re.sub(r"->", "$\\\Rightarrow$", v)),
    ]
    for f in funcs:
        for k, v in entity_local.items():
            if type(v) == list:
                entity_local[k] = map(lambda v: f(v), v)
            elif type(v) == str:
                entity_local[k] = f(v)
    return entity_local


def generate_entity_text(
    entity: ty.Entity,
    text_type: str = "md",
    html_characters: bool = False,
    include_full_text: bool = False,  # only used by .md right now..
    skip_feature_generation: bool = False,
    # TODO: this doesn't show up in the curly command and probably it should! and maybe some other ones too
    skip_table: bool = False,  # only used by .md right now..
    # TODO: the latex here is really only for cards... probably it should still be able to handle tables though
) -> str:
    entity_local = deepcopy(entity)
    if text_type == "md":
        if html_characters:
            # TODO: this is broken by having lists in the data..
            arrow = "&#8658;"
            for key in entity_local.keys():  # untested.. yet
                entity_local[key] = re.sub(r"[_]", r"\_", entity_local[key])
                entity_local[key] = re.sub(r"->", f"{arrow}", entity_local[key])
                entity_local[key] = re.sub("\*", r"\*", entity_local[key])
        md_text = generate_md(entity_local) if not skip_feature_generation else ""
        if include_full_text:
            md_text = tf.format_full_text_md(entity_local) + md_text + "  \n\n"
        if not skip_table:
            if "table" in entity.keys():
                md_text += tf.format_md_table(entity["table"])
        return md_text
    elif text_type == "latex":
        return generate_latex(prep_latex(entity_local))
    else:
        raise Exception("text_type needs to be either 'latex' or 'md'.")


# entity tree functions


def text_has_children(text: str) -> bool:
    return any([curly["entity"] for curly in p.parse_curlies(text)])


def get_replacement_text(
    base_text: str,
    curlies_parsed: list,
) -> str:
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


def generate_entity_tree_and_non_unique(
    db,
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
            entity = dt.fetch_by_name(db, curly["entity"])
            has_table = "table" in entity.keys()
            entity_text = generate_entity_text(
                entity,
                text_type="md",
                html_characters=html_characters,
                skip_table=roll_dice,
                # if we are rolling dice, then we dont want the whole table, instead we just handle the result of the table!
            )
            if roll_dice and has_table:  # now we handle that table we skipped!
                entity_text += (
                    f"Table Result:  \n" + du.roll_on_table(entity, curly) + "\n"
                )
            curlies_parsed = p.parse_curlies(entity_text)
            if any(
                [inner_curly["quantity_dice"] for inner_curly in curlies_parsed]
            ) or (has_table and roll_dice):
                unique = True
            else:
                unique = False
                # this uniqueness detection is not perfect!
                # two entities could end up rolling the same dice and/or have the same table result, so they would be identical, but both counted as "unique"
                # "uniqueness" here is an anticipation of inherent randomness/randomization, its not a guarantee of not-being-identical!
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
                curly_queue.append(p.parse_curlies(entity_text))
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


def generate_entity_tree_text(
    db,
    base_curly: ty.Curly,
    expand_entities: bool = False,
    roll_dice: bool = False,
    html_characters: bool = False,
) -> str:
    base_quantity = base_curly["quantity"]
    # just need this line for the fancy name:
    base_entity = dt.fetch_by_name(db, base_curly["entity"])
    base_entity_text = generate_entity_text(
        base_entity, html_characters=html_characters
    )
    if not expand_entities or not text_has_children(base_entity_text):
        if roll_dice:
            n_base_entity = str(base_quantity) + " " + base_entity["name"] + "  \n"
            curlies_parsed = p.parse_curlies(base_entity_text)
            return n_base_entity + get_replacement_text(
                base_text=base_entity_text, curlies_parsed=curlies_parsed
            )
        else:
            return base_entity_text
    entity_tree, non_unique_entities = generate_entity_tree_and_non_unique(
        db, base_curly, expand_entities, roll_dice
    )
    if not len(non_unique_entities) == 0:
        non_unique_text = """### Non Unique Entities:\n"""
        for clean_name, v in non_unique_entities.items():
            non_unique_text += f"\n{v['count']} {clean_name}  \n\n{v['text']}"
    else:
        non_unique_text = ""
    entity_text = """### Unique Entities, Full Tree:\n"""
    for n in entity_tree:
        if n["unique"]:
            entity_text += "\n" + n["text"]
    return (non_unique_text + "\n" + entity_text).strip()
