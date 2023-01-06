import os

from citutils import commands as co
from citutils import text_utils_parsers as tu

# this really only does cards at this point


def get_dl_path(filename: str) -> str:
    return os.path.join("data", "downloads", "cards", filename)


entities = tu.get_entities(os.path.join("data", "entities"))

## generating cards

### all
co.filter_generate_cards(entities, "poker", "", "", get_dl_path("all_cards"))
### basic
co.filter_generate_cards(entities, "poker", "basic", "", get_dl_path("basic_cards"))
### invocations
co.filter_generate_cards(
    entities, "poker", "invocation", "", get_dl_path("invocation_cards")
)
### items
co.filter_generate_cards(entities, "poker", "item", "", get_dl_path("item_cards"))
### npcs
co.filter_generate_cards(entities, "poker", "npc", "", get_dl_path("npc_cards"))
### skills
co.filter_generate_cards(entities, "poker", "skill", "", get_dl_path("skill_cards"))
### weapons
co.filter_generate_cards(entities, "poker", "weapon", "", get_dl_path("weapon_cards"))
