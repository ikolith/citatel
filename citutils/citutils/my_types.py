from typing import NewType, TypedDict, Union


class Curly(TypedDict):
    match: str
    quantity_dice: str
    table_dice: str
    entity: str
    quantity: int
    table_result: Union[int, None]


class Table(TypedDict, total=False):
    roll: str  # optional
    outcomes: dict[int, str]  # required
    # this optional/doable setup is doable in python 3.11...
    # but discord.py doesn't support 3.11,
    # so they're just all optional because total=False. Sad!


class Entity(TypedDict, total=False):
    attacks: list
    clean_name: str
    cost: str
    effect: str
    encumbrance: str
    flavor_text: str
    holds: str
    hp: str
    meta_tags: list
    name: str  # this would be required, everything else would be optional
    # if i could use python 3.11! discord.py!!!
    requirements: list
    scores: list
    skills: list
    speed: str
    tags: list
    target: str
    to_hit: str
    full_text: str
    table: Table


Entities = NewType("Entities", dict[str, Entity])


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


## The next types are from the old doc-generation workflow which will be removed soon.


class ES(TypedDict, total=False):
    text: str
    clean_name: str
    include_full_text: bool
    fi: str
    fx: str


ESs = NewType("ESs", list[ES])


class Doc(TypedDict, total=False):
    # not used anymore!
    entity_sections: ESs
    front_text: str
    end_text: str
    text_type: str
    html_characters: bool
    skip_feature_generation: bool


class DocPath(TypedDict, total=False):
    doc: Doc
    path: str


DocsToUpdate = NewType("DocsToUpdate", list[DocPath])
