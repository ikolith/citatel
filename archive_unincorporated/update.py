# TODO: this will require probably the most changing...
import citutils.citutils.entity_text_generators as ge
import citutils.citutils.text_utils_parsers as tu
import commands as co
import citutils.citutils.my_types as ty
import os
from datetime import date


def get_front_text(name: str, toc: bool = False) -> str:
    toc_text = "toc: true" if toc else ""
    return rf"""---
title: {name}
{toc_text}
---

"""

end_text = f"This file was last auto-generated on {date.today()}."


def write(text: str, path: str) -> None:
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(text)


def md_updater(entities: ty.Entities, to_update: ty.DocsToUpdate) -> None:
    for update in to_update:
        write(ge.generate_doc_text(entities, **update["doc"]), update["path"])


# Docs

basic_doc = ty.Doc(
    {
        "entity_sections": ty.ESs(
            [
                ty.ES({"text": "## Basic Skills", "fi": "skill, basic"}),
                ty.ES({"text": "## Basic Weapons", "fi": "weapon, basic"}),
                ty.ES(
                    {
                        "text": "## Basic Items",
                        "fi": "item, basic",
                    }
                ),
                # didnt choose to include invocations and npcs, didnt seem to make much sense to do so
            ]
        ),
        "front_text": r"""---
title: Basic Entities
toc: true
---

This is a collection of all the basic weapons, skills, and items. No spoilers here.

""",  # More pre-made pages and cards are available at the [downloads page](../code_and_downloads/downloads.md).
        "end_text": end_text,
        "text_type": "md",
        "html_characters": True,
    }
)

## NPC docs

legion_doc = ty.Doc(
    {
        "entity_sections": ty.ESs(
            [ty.ES({"clean_name": "legion", "include_full_text": True})]
        ),
        "front_text": get_front_text("Legions"),
        "end_text": end_text,
        "html_characters": True,
        "skip_generation": True,
    }
)
#
tchok_doc = ty.Doc(
    {
        "entity_sections": ty.ESs(
            [ty.ES({"clean_name": "tchok", "include_full_text": True})]
        ),
        "front_text": get_front_text("Tchoks"),
        "end_text": end_text,
        "html_characters": True,
    }
)
# docs_to_update = ty.DocsToUpdate(
#     [
#         ty.DocPath(
#             {
#                 "doc": tchok_doc,
#                 "path": os.path.join(".", "docs", "_npcs_and_factions", "tchoks.md"),
#             }
#         ),
#         ty.DocPath(
#             {
#                 "doc": legion_doc,
#                 "path": os.path.join(".", "docs", "_npcs_and_factions", "legions.md"),
#             }
#         ),
#         ty.DocPath(
#             {
#                 "doc": basic_doc,
#                 "path": os.path.join(".", "docs", "_pages", "talaje", "basic.md"),
#             }
#         ),
#     ]
# )
