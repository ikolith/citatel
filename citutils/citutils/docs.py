# """ mishmash of scripts to dynamically generate docs
# because I don't have time to do it all manually."""

import os

from tinydb import Query

import citutils.text_generators as ge
import citutils.database as dt

# md


def create_query_section(
    db_path=os.path.join("..", "..", "source.json"),
    query=Query(),  # how do i type this
    text_type="md",  # enum "md" or "latex"
    # basic: bool = False,  # im lazy.
    sort: bool = True,
    deprecated: bool = False,
) -> str:
    if not deprecated:
        query = query & ~Query().meta_tags.any("deprecated")
    db = dt.create_tinydb(db_path)
    # if basic:
    #     query = query & Query().meta_tags.any("basic")
    results = db.search(query)
    if sort:
        results = sorted(results, key=lambda x: x["name"])
    text = ""
    for e in results:
        text += ge.generate_entity_text(e, text_type, True, True, False) + "\n"
    return text
