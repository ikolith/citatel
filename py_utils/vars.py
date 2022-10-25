# TODO: all of these need to be fixed for the csv -> yaml switch... gonna just have to ctrl f this one to fix it

from typing import NewType, TypedDict

# types

Entities = NewType("Entities", dict[str, dict[str, str]])

# should be:...
# [{"text": "text",
#  "filter_tags_include":"",
# "filter_tags_exclude":"",
# "clean_name":""},{...}...]


# TODO: once discord.py has new fresh wheels and is functional again ill implement the python 3.11 advanced dict nonsense... and ill put off really getting mypy in until that point anyway too.. ohwell
# class EntityFilterSections(TypedDict):
#     text: NotRequired[str]


cli_curly_help = """ TODO: rewrite this so it's in standard cli format.
    
    "curly" parses input as if it is within curly braces ({}).
Input within curly braces consists of two optional parts, a die roll and an entity.

Die rolls:
Die rolls look like "(A)dB(x)(+ or - some integer)" where anything in parentheses is optional.
A: The number of dice, if this is left blank, it will be assumed you wanted one die.
B: The top face of the die.
x: Optional. Specifies whether the dice are "exploding", that is, rolling a max value will cause you to roll another die.
+ or -: allows you to add or subtract some non-fraction from the result.

Entities:
An entity is any valid entry in the csvs that the entities function can see. You do not have to specify whether the entity is an npc, weapon, etc. That is handled automatically.

A valid input can be one of the following:
- A die roll. Ex: {d3}, {9d9x-10}.
- An entity. Ex: {greatsword}, {shady_merchant}.
- A die roll that determines the number of entities. Ex {3d100 gold_coins}, {2d4x footsoldiers}.
- Or a specified number of entities. Ex: {100 gold_coins}, {6 footsoldiers}. 

The following are not valid inputs:
- {7}. It's just a number, what would the parser even do in this situation?
- {greatsword 99}. Wrong roll-entity order.
- {footsoldier d6}. Wrong roll-entity order.
- {2 d6}. Looks like you want two entities called d6. This would actually work if there were an entity present called d6, but that's a terrible name for an entity, and that's probably not the behaviour you wanted. 

The flag -e or --expand_entities specifies that you want entities within your the given entity to be expanded and processed along with any entities within those entities and so on.

The flag -r or --roll_dice specifies that you want any dice within a generated entity to be rolled and processed.

When you give an input you can leave the curlies off if you would like, the stated function is to emulate programmatic curly parsing, so the curly braces are optional.

Note: I'm using the same text for the cli and the bot because there's no significant difference. The bot doesn't use flags but fixed arguments, that's it. They have the same default behaviours.
"""

cli_card_size_help = """ Use -t to specify one of the card sizes "tarot", "poker", or "square".
"poker" gives you 9 cards per sheet at 89mm.
"tarot" gives 6 cards per sheet at 110mm.
"square" gives 12 cards per sheet at 64mm.
"poker" is the default.
"""

bot_enlist_help = """/enlist lets you create a list of entities that you can pass to the cards command instead of having to manually name all the cards you want.

Leaving every field blank will create a list of all entities with the default name, "enlist".

filter_tags_include: This allows you to filter for only entities that have one of the filter tags given. 

filter_tags_exclude: This allows you to only get entities that do *not* have the given filter tags.

filter_tags are in the filter_tag column of the entity csvs.

Common filter tags are:

- "basic" which specifies entities that you would know about at the beginning of the game. "basic" allows you to avoid spoilers. 

- "large" which is used to tag entities with too much text to fit in the standard poker size card. At the moment the only entities that large are complex magic skills.

- "weapon", "npc", "item" etc.
"""

bot_cards_help = """/cards lets you create cards, they will be sent in the form of a pdf called "cards.pdf" in the reply to the command.

There are three arguments, you only need to give it one or two. 

list_name: This is the name of some list created by /enlist. The default list name is "enlist", if you want that list you can just call it "e" and that will be corrected to "enlist" here. This will override the cards parameter. If a comma separated list of entities is provided in "cards" as well as a list_name, only the list_name will matter. TODO: they should probably just be combined.

cards: This is a comma separated list of entity clean_names. Something like "sword,arrow,horse,skeleton". One card will be made for each entity. 

card_type: This is the size of each card, "tarot", "poker","square" or "quarter". The default is "poker".
"poker" gives you 9 cards per sheet at 89mm.
"tarot" gives 6 cards per sheet at 110mm.
"square" gives 12 cards per sheet at 64mm.
"quarter" gives 4 cards per sheet at around 100mm, gets tweaked sometimes.
"""

all_entities_front_matter = """---
title : Generated Markdown for All Entities
toc : True
---
<!-- Don't try to edit this file directly, there is no point. This is generated using the all_entities_md() function in (starting at the top of the whole project) py_utils/entity_text_generators.py-->

## Spoilers Ahead

This page tchok-full of spoilers. This is all the content in the entity tables (as of the last time I generated this doc, of course). If you want to avoid spoilers and/or filter the entities you see, the currently available tools are the discord bot and the Python command line interface in the repo (cli.py).

There will probably be better online documentation generators down the line. This is here for the sake of completeness and because I thought it couldn't be *that* hard to get them all up here.

"""

# doc dicts for generate doc_text
