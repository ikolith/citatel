import pandas as pd
from pylatex.utils import NoEscape
import py_utils.vars as v
import os
from collections.abc import Callable

# single entity text generators. used for cli and various utilities.

# start of latex formatting section
smallskip = r"\smallskip "
skipline = smallskip + r" \hrule " + smallskip


def curry_wrap(latex: str) -> str:  # latex formatting wrapper
    """Sidëf̈ect: sounds delicious."""
    return lambda text: "\\" + latex + r"{" + text + r"}"


bold = curry_wrap("textbf")
italic = curry_wrap("textit")
large = curry_wrap("large")
f_note = curry_wrap("footnotesize")
s_cap = curry_wrap("textsc")
t_normal = curry_wrap("textnormal")
emph = curry_wrap("emph")

# latex section formatting


def if_field_exists_latex(
    text: str, field_text: str = "", end_with_newline: bool = True
) -> str:
    if text:
        return emph(field_text) + text
    else:
        return ""


def if_exists(text: str) -> str:
    return text if text else ""


def name_latex(text: str) -> str:
    return bold(large(text))


def flavor_latex(text: str) -> str:
    return skipline + italic(text) if text else ""


# flushright and...
def tag_latex(text: str) -> str:
    return f_note("Tags: " + text) + "\n" + r" \normalsize" + "\n\n"


def attacks_latex(attacks: str) -> str:
    attacks = attacks.replace("::", r" \newline ")
    attacks_list = attacks.split(",")
    itemized_attacks = ""
    for attack in attacks_list:
        itemized_attacks += "    \item " + attack + "\n"
    return (
        skipline
        + emph(r"Attacks: ")
        + "\n"
        + r"\begin{itemize}"
        + "\n"
        + rf"{itemized_attacks}"
        + "\n"
        + r"\end{itemize}"
    )  # do not need to line break after this ending an itemize creates a line break


def skill_effect_latex(text: str) -> str:
    return NoEscape(
        skipline
        + text.replace(
            "::",
            "\n" + r" \medskip" + "\n",
        )
    )


def footer_latex(clean_name: str, encumbrance: str = ""):
    enc = f_note("Enc: " + encumbrance) if encumbrance else ""
    return rf""" \vfill
    {f_note(clean_name)} \hfill {enc}"""


# latex entity text generation


def generate_invocation_latex(row: pd.Series) -> str:
    return NoEscape(
        name_latex(row["name"])
        + if_field_exists_latex(row["target"], "Target: ")
        + skipline
        + if_field_exists_latex(row["effect"])
        + flavor_latex(row["flavor_text"])
        + footer_latex(row["clean_name"])
    )


def generate_item_latex(row: pd.Series) -> str:
    return NoEscape(
        name_latex(row["name"])
        + row["effect"]
        + flavor_latex(row["flavor_text"])
        + footer_latex(row["clean_name"], row["encumbrance"])
    )


def generate_npc_latex(row: pd.Series) -> str:
    return NoEscape(
        name_latex(row["name"])
        + if_field_exists_latex(row["hp"], "HP: ")
        + if_field_exists_latex(row["scores"], "Scores: ")
        + if_field_exists_latex(row["skills"], "Skills: ")
        + if_field_exists_latex(row["holds"], "Holds: ", False)
        + if_field_exists_latex(flavor_latex(row["flavor_text"]))
        + footer_latex(row["clean_name"])
    )


def generate_weapon_latex(row: pd.Series) -> str:
    return NoEscape(
        name_latex(row["name"])
        + tag_latex(row["tags"])
        + if_field_exists_latex(row["requirements"], "Requirements: ")
        + if_field_exists_latex(row["speed"], "Speed: ")
        + if_field_exists_latex(row["to_hit"], "To-Hit: ", False)
        + attacks_latex(row["basic_attacks"])
        + if_exists(if_field_exists_latex(row["effect"], "", False))
        + flavor_latex(row["flavor_text"])
        + footer_latex(row["clean_name"], row["encumbrance"])
    )


def generate_skill_latex(row: pd.Series) -> str:
    return NoEscape(
        name_latex(row["name"])
        + if_field_exists_latex(row["requirements"], "Requirements: ")
        + if_field_exists_latex(row["cost"], "Cost: ")
        + skill_effect_latex(row["effect"])
        + footer_latex(row["clean_name"])
    )


def if_exists_format_latex(
    text: str,
    text_formatter: Callable = None,
    field_text: str = "",
    field_text_formatter: Callable = None,
    add_newline: bool = True,
    add_skipline: bool = False,
    hide: bool = False,
) -> str:
    if hide:
        return ""
    newline = " \n \n" if add_newline else ""
    skipline = skipline if add_skipline else ""
    if field_text:
        return field_text_formatter(field_text) + " " + text + newline
        # field_text_formatter here will often be emph()
    elif text_formatter:
        return text_formatter(text) + newline


formatting_dict_latex = {
    "basic_attacks": {"text_formatter": attacks_latex},
    "cost": {"field_text": "Cost", "field_text_formatter": emph},
    "effect": {},
    "encumbrance": {"field_text": "Encumbrance", "field_text_formatter": emph},
    #need to put this and maybe encumbrance on the footer..
    "filter_tags": {"hide": True},
    "flavor_text": {"text_formatter": lambda text: skipline + italic(text)},
    "holds": {"field_text": "Holds", "field_text_formatter": emph},
    "hp": {"field_text": "HP", "field_text_formatter": emph},
    "name": {"text_formatter": lambda text: bold(large(text))},
    "requirements": {"field_text": "Requirements", "field_text_formatter": emph},
    "scores": {"field_text": "Scores", "field_text_formatter": emph},
    "skills": {"field_text": "Skills", "field_text_formatter": emph},
    "speed": {"field_text": "Speed", "field_text_formatter": emph},
    "tags": {"field_text": "Tags", "field_text_formatter": emph},
    "target": {
        "field_text": "Target",
        "field_text_formatter": emph,
        "add_skipline": True,
    },
    "to_hit": {"field_text": "To-Hit", "field_text_formatter": emph},
}


def generate_latex(entity: dict, formatting: dict = formatting_dict_latex) -> str:
    result_text = ""
    for key, text in entity.items():
        result_text += if_exists_format_latex(
            text=str(text), **formatting_dict_latex[key]
        )
    
    return result_text


# md generation


def if_exists_format_md(
    text: str,
    text_wrapper: str = "",
    prefix: str = "",
    field_text: str = "",
    field_wrapper: str = "**",
    newline: bool = True,
    hide: bool = False,
) -> str:
    if hide:
        return ""
    newline = "  \n" if newline else ""
    if field_text:
        return field_wrapper + field_text + ":" + field_wrapper + " " + text + newline
    elif prefix:
        return prefix + " " + text + newline
    return text_wrapper + text + text_wrapper + newline


#     row["basic_attacks"] = row["basic_attacks"].replace(",", "\n-")
formatting_dict_md = {
    "basic_attacks": {},
    "cost": {"field_text": "Cost"},
    "effect": {},
    "encumbrance": {"field_text": "Encumbrance"},
    "filter_tags": {"hide": True},
    "flavor_text": {"text_wrapper": "*"},
    "holds": {"field_text": "Holds"},
    "hp": {"field_text": "HP"},
    "name": {"prefix": "### "},
    "requirements": {"field_text": "Requirements"},
    "scores": {"field_text": "Scores"},
    "skills": {"field_text": "Skills"},
    "speed": {"field_text": "Speed"},
    "tags": {"field_text": "Tags"},
    "target": {"field_text": "Target"},
    "to_hit": {"field_text": "To-Hit"},
}


def generate_md(entity: dict, formatting: dict = formatting_dict_md) -> str:
    result_text = ""
    for key, text in entity.items():
        result_text += if_exists_format_md(text=str(text), **formatting_dict_md[key])
    return result_text


def generate_entity_text(
    entity: dict,
    text_type: str = "md",
    html_characters: bool = False,
) -> str:
    if text_type == "md":
        text = generate_md(entity)
        # if html_characters:
        #     arrow = "&#8658;"
        #     empty_triangle_r = "&#9655;"
        #     filled_triangle_r = "&#9654;"
        #     triangle_up = "&#9650;"
        #     row = row.str.replace(
        #         r"[_]", r"\_", regex=True
        #     )
        #     row = row.str.replace(r"->", f"{arrow}", regex=True)

        #     row = row.str.replace(
        #         r"\[swinging: following]",
        #         f"{filled_triangle_r} {empty_triangle_r} {empty_triangle_r}",
        #         regex=True,
        #     )
        #     row = row.str.replace(
        #         r"\[swinging: neutral]",
        #         f"{empty_triangle_r} {filled_triangle_r} {empty_triangle_r}",
        #         regex=True,
        #     )
        #     row = row.str.replace(
        #         r"\[swinging: leading]",
        #         f"{empty_triangle_r} {empty_triangle_r} {filled_triangle_r}",
        #         regex=True,
        #     )
        #     row = row.str.replace(
        #         r"\[thrusting]",
        #         f"{triangle_up}",
        #         regex=True,
        #     )

    if text_type == "latex":
        # row = row.str.replace(r"[{}]", "", regex=True)
        # row = row.str.replace(r"[_]", r"\_", regex=True)
        # row = row.str.replace(r"->", "$\\\Rightarrow$", regex=True)
        # # replacing text with latex glyphs for the [swinging: ...], [thrusting] tags
        # row = row.str.replace(
        #     r"\[swinging: following]",
        #     r"$\\blacktriangleright\\mkern-7mu\\triangleright\\mkern-7mu\\triangleright$",
        #     regex=True,
        # )
        # row = row.str.replace(
        #     r"\[swinging: neutral]",
        #     r"$\\triangleright\\mkern-7mu\\blacktriangleright\\mkern-7mu\\triangleright$",
        #     regex=True,
        # )
        # row = row.str.replace(
        #     r"\[swinging: leading]",
        #     r"$\\triangleright\\mkern-7mu\\triangleright\\mkern-7mu\\blacktriangleright$",
        #     regex=True,
        # )
        # row = row.str.replace(
        #     r"\[thrusting]",
        #     r"$\\blacktriangle$",
        #     regex=True,
        # )

        text = generate_latex(entity)
    return text


# TODO rewrite this for the new system
def all_entities_md(
    all_data: dict,
    html_characters: bool = False,
    output_filepath: str = os.path.join(
        "docs", "_pages", "talaje", "generated_entities.md"
    ),
    front_matter=v.all_entities_front_matter,
) -> None:
    contents = front_matter
    for entity_type in all_data:
        contents += "## " + entity_type.capitalize() + "  \n\n"
        df = all_data[entity_type].sort_index()
        for index, row in df.iterrows():
            contents += (
                generate_entity_text(entity_type, row, "md", html_characters)
                + "\n  "
                + "\n  "
                + "--- \n"
            )
    with open(output_filepath, "w") as f:
        f.write(contents)
