from typing import NewType, TypedDict

# mypy doesn't want this called "types.py". fine.


class Curly(TypedDict):
    match: str
    roll: str
    entity: str
    quantity: int


Entity = NewType("Entity", dict[str, str])
Entities = NewType("Entities", dict[str, Entity])


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
