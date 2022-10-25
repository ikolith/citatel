import py_utils.entity_text_generators as g
import py_utils.text_utils_parsers as t
import py_utils.vars as v
import os
from datetime import date

entities = t.get_entities(os.path.join("docs", "_data", "entities"))

end_text = f"This file was last auto-generated on {date.today()}."


def write(text: str, path: str) -> None:
    with open(path, mode="w") as f:
        f.write(text)


def md_updater(entities: v.Entities, to_update: list) -> None:
    for update in to_update:
        write(g.generate_doc_text(entities, **update["doc"]), update["path"])


# def card_updater():
#    pass

basic_docs = {
    "entity_filter_sections": [
        {"text": "## Basic Skills", "fi": "skill, basic"},
        {"text": "## Basic Weapons", "fi": "weapon, basic"},
        {
            "text": "## Basic Items",
            "fi": "item, basic",
        },
        # didnt choose to include invocations and npcs, didnt seem to make much sense to do so
    ],
    "front_text": r"""---
title: Basic Entities
toc: true
---

This is a collection of all the basic weapons, skills, and items. No spoilers here. More pre-made pages and cards are available at the [downloads page](../code_and_downloads/downloads.md).

""",
    "end_text": end_text,
    "text_type": "md",
    "html_characters": True,
}

docs_to_update = [
    {
        "doc": basic_docs,
        "path": os.path.join(".", "docs", "_pages", "talaje", "basic.md"),
    },
    {
        "doc": basic_docs,
        "path": os.path.join(".", "docs", "_pages", "talaje", "basic.md"),
    },
]

md_updater(entities, docs_to_update)
