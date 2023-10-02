#!/usr/bin/env python3
import argparse
import os.path

try:
    from citutils import parsers as tu, vars as vs, commands as co
except:
    print("citutils not found. Have you tried running . .venv/bin/activate ?")
    exit()

entities = tu.get_entities(os.path.join("data", "entities"))

# subparsers

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")
subparsers.add_parser(
    "help",
    help="Show this help message and exit. Still need more help? Try calling the various commands with the --help flag to get better explanations of them and their options. #TODO: make help messages better.",
)

curly_p = subparsers.add_parser(
    "curly",
    help="Evaluate a string as a single curly. Example: curly 'salt wretch' will evaluate to the info block of the salt wretch.",
)
curly_p.add_argument(
    "curly",
    type=str,
    help=vs.cli_curly_help,
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

card_p = subparsers.add_parser("cards", help="I guess this makes cards or something.")
card_p.add_argument("cards", type=str, nargs="?", help="TODO: explain how this works")
card_p.add_argument(
    "-t",
    "--type",
    action="store",
    help=vs.cli_card_size_help,
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
    help="""Use "enlist" to create a .txt list of entities. By default all entities will be gathered and the output file will be at output/entities.txt""",
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


# As cli...
if __name__ == "__main__":
    args = parser.parse_args()
    if args.command == None or args.command == "help":
        parser.print_help()
        # for subparser in [curly_p, card_p, enlist_p]: # Something like this kind of thing is probably a good idea, but as it stands the output is just too large.
        # subparser.print_help()
    if args.command == "curly":
        print(
            tu.single_curly_parser(
                entities, args.curly, args.expand_entities, args.roll_dice
            )
        )

    elif args.command == "cards":
        co.enlist_generate_cards(
            entities, args.type, args.cards, args.input_filepath, args.output_filepath
        )

    elif args.command == "enlist":
        co.enlist(
            entities,
            args.filter_tags_include,
            args.filter_tags_exclude,
            args.output_filepath,
        )
