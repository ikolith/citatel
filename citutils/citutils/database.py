import json
import os
from functools import reduce
import re

from tinydb import TinyDB, where, Query

import citutils.my_types as ty
import citutils.parsers as p


def create_tinydb(input_path: str = "source.json", output_path: str = "db.json"):
    """This function creates a flattened TinyDB db.
    !!! You should not write to this db !!!
    !!! The db is overwritten every time the function is run !!!
    The db does not preserve any hierarchy or table information.
    The function creates a db that is meant to be used only for querying, code functionality.
    This may be changed in the future.
    """

    def build_db(data):
        for k, v in data.items():
            if "name" in v:
                v["clean_name"] = p.get_clean_name(v["name"])
                db.insert(v)
            else:
                build_db(v)

    def get_expanded_outcomes(table: ty.Table):
        expanded_outcomes = {}
        for k, v in table["outcomes"].items():
            if type(k) == str and (match_k := re.search(r"(\d*)-(\d*)", k)) is not None:
                start, end = match_k.groups()
                for new_k in range(int(start), int(end) + 1):
                    expanded_outcomes[int(new_k)] = v
            else:
                expanded_outcomes[int(k)] = v
        table["expanded_outcomes"] = expanded_outcomes
        return table

    if os.path.exists(output_path):
        os.remove(output_path)
    db = TinyDB(output_path)

    with open(input_path, "r") as f:
        data = json.load(f)

    build_db(data)

    for doc in db.all():
        if "table" in doc.keys():
            table = get_expanded_outcomes(doc["table"])
            db.update({"table": table}, doc_ids=[doc.doc_id])
            if "roll" not in doc["table"].keys():
                table["roll"] = "1d" + str(max(table["expanded_outcomes"].keys()))
                db.update({"table": table}, doc_ids=[doc.doc_id])
    return db


def fetch_by_name(db, name: str):  # TODO: typing! get that mypy typing moving
    """Fetches an entity by name by first converting it to clean_name.
    As a result, passing a clean_name is fine too.
    This function should not change even if the db does.
    """
    # I really dont love this. Wish TinyDB let me set an index.
    result = db.search(where("clean_name") == p.get_clean_name(name))
    assert len(result) == 1
    return result[0]


def get_unique_array_field_values(db):
    unique_field_values = {}  # {..., "FIELDNAME": set()}
    for doc in db.all():
        for k, v in doc.items():
            if isinstance(v, list):
                if k not in unique_field_values:
                    unique_field_values[k] = set()
                for i in v:
                    unique_field_values[k].add(i)
    for k, v in unique_field_values.items():
        unique_field_values[k] = list(sorted(v))
    return unique_field_values


def filter_entities(db, fields: list, params: list[list | str]):
    query = Query()
    assert len(fields) == len(params)
    field = fields[0]
    param = params[0]

    if len(fields) == 1:
        if isinstance(param, str):
            return db.search(query[field] == param)
        else:
            return db.search(query[field].all(param))

    if isinstance(param, str):
        final_query = query[field] == param
    else:
        final_query = query[field].all(param)

    for field, param in zip(fields[1:], params[1:]):
        if isinstance(param, str):
            condition = query[field] == param
        else:
            condition = query[field].all(param)
        final_query = final_query & condition

    # Use the final_query to search the database
    return db.search(final_query)
