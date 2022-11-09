import py_utils.my_types as ty
import py_utils.cards as cr
import py_utils.text_utils_parsers as tu
import py_utils.dice_utils as du
import warnings
from copy import deepcopy
import os


def filter_entities_by_filter_tags(
    entities: ty.Entities,
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
) -> ty.Entities:
    # enlist only uses the clean names, so filtered_entities.keys() but we build the entire dict for... futureproofing???
    fti = filter_tags_include.replace(" ", "").split(",") if filter_tags_include else []
    ftx = filter_tags_exclude.replace(" ", "").split(",") if filter_tags_exclude else []
    filtered_entities = ty.Entities({})
    for clean_name, entity in entities.items():
        if "filter_tags" not in entity.keys():  # untested
            if not fti:
                filtered_entities[clean_name] = entity
                continue
            else:
                continue
        filter_tags = entity["filter_tags"].replace(" ", "").split(",")
        if ftx:
            if any(ft in ftx for ft in filter_tags):
                # possibly users should be able to choose between any() and all() as filtering behaviour...
                continue
        if fti:
            if all(ft in filter_tags for ft in fti):
                filtered_entities[clean_name] = entity
        else:
            filtered_entities[clean_name] = entity
    return filtered_entities


def enlist(
    entities: ty.Entities,
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
    output_filepath: str = "",
) -> None:
    enlist_entities = deepcopy(entities)  # seems kinda heavy for this...
    if filter_tags_include or filter_tags_exclude:
        enlist_entities = filter_entities_by_filter_tags(
            enlist_entities, filter_tags_include, filter_tags_exclude
        )
    if not output_filepath:
        output_filepath = os.path.join("output", "entities.txt")
    enlist = ",".join(list(enlist_entities.keys()))
    if not enlist:
        warnings.warn(
            "No entities will be written. Consider checking your filters and requested type."
        )
    with open(output_filepath, mode="w") as f:
        f.write(enlist)


def filter_generate_cards(
    entities: ty.Entities,
    card_type: str = "",
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
    output_filepath: str = os.path.join("output", "filter_cards"),
) -> None:
    card_entities = list(
        filter_entities_by_filter_tags(
            entities, filter_tags_include, filter_tags_exclude
        ).keys()
    )
    cr.generate_cards(card_entities, entities, card_type, output_filepath)


def enlist_generate_cards(
    entities: ty.Entities,
    card_type: str = "",
    cards: str = "",
    input_filepath: str = "",  # maybe this should just be replaced with fi/fx tbh
    output_filepath: str = "",
) -> None:
    # set card type
    card_type = "poker" if not card_type else card_type
    # get entity list either from file or passed arguments
    if input_filepath:
        if input_filepath == "e":
            input_filepath = os.path.join("output", "entities.txt")
            # just a little shortcut to the default
        with open(input_filepath) as f:
            card_entities = f.readline().split(sep=",")
    else:
        card_entities = cards.split(",")
    assert card_entities
    if not output_filepath:
        output_filepath = os.path.join("output", "cards")
    cr.generate_cards(card_entities, entities, card_type, output_filepath)


def single_curly_parser(
    text: str,
    entities: ty.Entities,
    expand_entities: bool = False,
    roll_dice: bool = False,
) -> str:
    if not (text.startswith("{") and text.endswith("}")):
        text = "{" + text + "}"
    curlies_parsed = tu.parse_curlies(text)
    assert len(curlies_parsed) == 1
    base_curly = curlies_parsed[0]
    # case when only die roll is present
    if not base_curly["entity"]:
        return str(du.die_parser_roller(base_curly["roll"]))

    # all other cases
    return tu.generate_entity_tree_text(
        base_curly, entities, expand_entities, roll_dice
    )
