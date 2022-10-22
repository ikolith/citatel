import argparse
import os.path
import pandas as pd
from copy import deepcopy
import warnings
import py_utils.text_utils as t
import py_utils.dice_utils as d
import py_utils.vars as v
import py_utils.minipages as m
import py_utils.entity_text_generators as g
from pprint import pprint

# TODO: move commands to commands.py

entities = t.get_entities(os.path.join("docs", "_data", "entities"))


def filter_entities_by_filter_tags(
    entities: dict[dict],
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
) -> dict[dict]:
    # enlist only uses the clean names, so filtered_entities.keys() but we build the entire dict for... futureproofing???
    fti = filter_tags_include.replace(" ", "").split(",") if filter_tags_include else []
    ftx = filter_tags_exclude.replace(" ", "").split(",") if filter_tags_exclude else []
    filtered_entities = {}
    for clean_name, entity in entities.items():
        if "filter_tags" not in entity.keys():  # untested
            if not fti:
                filtered_entities[clean_name] = entity
            else:
                continue
        filter_tags = entity["filter_tags"].replace(" ", "").split(",")
        if ftx:
            if any(ft in ftx for ft in filter_tags):
                continue
        if fti:
            if any(ft in fti for ft in filter_tags):
                # could also do set(a) & set(b) but that seems likely slower? at least, less readable
                filtered_entities[clean_name] = entity
        else:
            filtered_entities[clean_name] = entity
    return filtered_entities


def cli_single_curly_parser(
    text: str, entities: dict[dict], expand_entities: False, roll_dice: False
) -> str:
    if not (text.startswith("{") and text.endswith("}")):
        text = "{" + text + "}"
    curlies_parsed = t.parse_curlies(text)
    assert len(curlies_parsed) == 1
    base_curly = curlies_parsed[0]

    # case when only die roll is present
    if not base_curly["entity"]:
        return str(d.die_parser_roller(base_curly["roll"]))

    # all other cases
    return t.generate_entity_tree_text(base_curly, entities, expand_entities, roll_dice)


def enlist(
    entities: dict[dict],
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
    output_filepath: str = None,
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


def command_generate_cards(
    card_type: str = None,
    cards: str = None,
    input_filepath: str = None,
    output_filepath: str = None,
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
    m.generate_cards(card_entities, entities, card_type, output_filepath)


# subparsers

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

curly_p = subparsers.add_parser("curly")
curly_p.add_argument(
    "curly",
    type=str,
    help=v.cli_curly_help,
)
curly_p.add_argument(
    "-e",
    "--expand_entities",
    action="store_true",
    help="Expand entities within a generated entity.",
)
curly_p.add_argument(
    "-r",
    "--roll_dice",
    action="store_true",
    help="Roll dice during entity generation if an entity is detected.",
)

card_p = subparsers.add_parser("cards")
card_p.add_argument("cards", type=str, nargs="?", help="TODO: explain how this works")
card_p.add_argument(
    "-t",
    "--type",
    action="store",
    help=v.cli_card_size_help,
)
card_p.add_argument(
    "-i",
    "--input_filepath",
    help="""Use the -i flag if you want to pass a .txt file containing just clean_names separated by commas. Example:
    a_sword,a_hat,a_potion,three_tchoks_in_a_trenchcoat
    "e" is an alias for ./output/entities.txt which is the default location that enlist will drop entities into, so you can use "-i e" to save a bit of typing if you used the default filepath for enlist.
    """,
)
card_p.add_argument(
    "-o",
    "--output_filepath",
    action="store_true",
    help="""Use the -o flag to specify an output pdf name. The default is "cards.pdf".""",
)
# Consider adding something to deal with entities with the "large" filter_tag

enlist_p = subparsers.add_parser(
    "enlist",
    help="""TODO: improve this
Use "enlist" to create a .txt list of entities. By default all entities will be gathered and the output file will be at output/entities.txt""",
)
enlist_p.add_argument(
    "-fi",
    "--filter_tags_include",
    help="""Enlist entities matching some set of filter_tags
    Example: -t weapons.""",
)
enlist_p.add_argument(
    "-fx",
    "--filter_tags_exclude",
    help="""Enlist entities matching some set of filter_tags
    Example: -t weapons.""",
)
enlist_p.add_argument(
    "-o",
    "--output_filepath",
    help="""Where the .txt should be written and what it should be named. By default it will be written at output/entities.txt""",
)

if __name__ == "__main__":
    args = parser.parse_args()
    if args.command == "curly":
        print(
            cli_single_curly_parser(
                args.curly, entities, args.expand_entities, args.roll_dice
            )
        )

    elif args.command == "cards":
        command_generate_cards(
            args.type, args.cards, args.input_filepath, args.output_filepath
        )

    elif args.command == "enlist":
        enlist(
            entities,
            args.filter_tags_include,
            args.filter_tags_exclude,
            args.output_filepath,
        )
