from typing import NewType, TypedDict, Union

# mypy doesn't want this called "types.py". fine.


class Curly(TypedDict):
    entity: str
    quantity_roll: str
    quantity_result: int
    determiner_roll: str
    determiner_result: str


class Table(TypedDict, total=False):
    roll: str  # this should be optional
    outcomes: dict[int, str]  # required
    filter_tags: str  # optional
    # this is doable in python 3.11...
    # but discord.py doesn't support 3.11,
    # so they're just all optional


Entity = NewType("Entity", dict[str, str])
Entities = NewType("Entities", dict[str, Union[Entity, Table]])


class ES(TypedDict, total=False):
    text: str
    clean_name: str
    include_full_text: bool
    fi: str
    fx: str


ESs = NewType("ESs", list[ES])


class Doc(TypedDict, total=False):
    # because total=False, none of these are required
    # possible this should be revised because of how totality affects inheritance...
    entity_sections: ESs
    front_text: str
    end_text: str
    text_type: str
    html_characters: bool
    skip_generation: bool


class DocPath(TypedDict, total=False):
    doc: Doc
    path: str


DocsToUpdate = NewType("DocsToUpdate", list[DocPath])


class NonUniqueEntity(TypedDict):
    text: str
    count: int


NonUniqueEntities = NewType("NonUniqueEntities", dict[str, NonUniqueEntity])


class TreeEntry(TypedDict):
    id: int
    entity: str
    children: list[int]
    unique: bool
    text: str
    curly: Curly


EntityTree = NewType("EntityTree", list[TreeEntry])
