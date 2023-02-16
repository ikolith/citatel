import warnings
from copy import deepcopy
import os

from citutils import (
    my_types as ty,
    dice_utils as du,
    text_utils_parsers as tu,
    cards as cr,
)

# im not sure that these should be organized in "commands"...


def filter_entities_by_filter_tags(
    entities: ty.Entities,
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
) -> ty.Entities:
    # enlist only uses the clean names, so filtered_entities.keys() but we build the entire dict for... futureproofing???
    fi = filter_tags_include.replace(" ", "").split(",") if filter_tags_include else []
    fx = filter_tags_exclude.replace(" ", "").split(",") if filter_tags_exclude else []
    filtered_entities = ty.Entities({})
    for clean_name, entity in entities.items():
        if "filter_tags" not in entity.keys():  # untested
            if not fi:
                filtered_entities[clean_name] = entity
                continue
            else:
                continue
        filter_tags = entity["filter_tags"].replace(" ", "").split(",")
        if fx:
            if any(ft in fx for ft in filter_tags):
                # possibly users should be able to choose between any() and all() as filtering behaviour...
                continue
        if fi:
            if all(ft in filter_tags for ft in fi):
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
    with open(output_filepath, mode="w", encoding="utf-8") as f:
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
    cr.generate_cards(entities, card_entities, card_type, output_filepath)


def enlist_generate_cards(
    entities: ty.Entities,
    card_type: str = "",
    cards: str = "",
    input_filepath: str = "",
    output_filepath: str = "",
) -> None:
    # set card type
    card_type = "poker" if not card_type else card_type
    # get entity list either from file or passed arguments
    if input_filepath:
        if input_filepath == "e":
            input_filepath = os.path.join("output", "entities.txt")
            # just a little shortcut to the default
        with open(input_filepath, encoding="utf-8") as f:
            card_entities = f.readline().split(sep=",")
    else:
        card_entities = cards.split(",")
    assert card_entities
    if not output_filepath:
        output_filepath = os.path.join("output", "cards")
    cr.generate_cards(entities, card_entities, card_type, output_filepath)
