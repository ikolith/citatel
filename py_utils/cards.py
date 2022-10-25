import re
import py_utils.text_utils_parsers as t
import py_utils.entity_text_generators as g
import os.path
from pylatex import Document, Command, MiniPage, UnsafeCommand, NewPage
from pylatex.base_classes import Arguments, Options, CommandBase
from pylatex.package import Package
from pylatex.utils import NoEscape


def generate_cards(
    card_entities: list,
    entities: dict[dict],
    card_type: str = "poker",
    output_filepath: str = os.path.join("cards", "cards"),
) -> None:
    cards_per_page = {"quarter": 4, "tarot": 6, "poker": 9, "square": 12}
    card_height = {
        "quarter": "130mm",
        "tarot": "110mm",
        "poker": "89mm",
        "square": "64mm",
    }
    card_width = {
        "quarter": "100mm",
        "tarot": "64mm",
        "poker": "64mm",
        "square": "64mm",
    }
    cards_per_row = {
        "quarter": 2,
        "tarot": 3,
        "poker": 3,
        "square": 3,
    }
    geometry_options = {"margin": ".07in"}
    if card_type not in cards_per_page.keys():
        raise ValueError("Invalid card type.")
    assert card_entities
    # define the LaTex command to generate a minipage of given dimensions, and populate it with content
    class CardCommand(CommandBase):
        _latex_name = "card"

    card_com = UnsafeCommand(
        "newcommand",
        "\card",
        options=3,
        extra_arguments=NoEscape(
            r"\fbox{\begin{minipage}[t][#1][t]{#2} #3 \end{minipage}}"
        ),
    )
    entity_texts = []
    for entity in card_entities:
        entity_texts.append(NoEscape(g.generate_entity_text(entities[entity], "latex")))
    # setup document and generate the preamble
    doc = Document(geometry_options=geometry_options, indent=False)
    doc.append(card_com)
    doc.packages.append(Package("fdsymbol"))
    for count, text in enumerate(entity_texts): 
        count += 1
        doc.append(
            CardCommand(
                arguments=Arguments(card_height[card_type], card_width[card_type], text)
            )
        )
        if count % cards_per_row[card_type] == 0 and count > 1:
            doc.append(NoEscape("\\newline"))
        if count % cards_per_page[card_type] == 0:
            doc.append(NewPage())
    doc.generate_pdf(output_filepath, clean_tex=False)
