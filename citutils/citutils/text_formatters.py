from collections.abc import Callable
import re

from pylatex.utils import NoEscape

import citutils.my_types as ty

# LATEX

# start of latex formatting section
smallskip = r"\smallskip "
skipline = smallskip + r" \hrule " + smallskip


def curry_wrap(latex: str) -> Callable[[str], str]:  # latex formatting wrapper
    """Sidëf̈ect: sounds delicious."""
    return lambda text: NoEscape("\\" + latex + r"{" + text + r"}")


bold = curry_wrap("textbf")
italic = curry_wrap("textit")
large = curry_wrap("large")
f_note = curry_wrap("footnotesize")
s_cap = curry_wrap("textsc")
t_normal = curry_wrap("textnormal")
emph = curry_wrap("emph")


def tag_latex(
    text: str,
) -> str:
    # havent gotten rid of this one because im not decided on whether ill use it, not using it for now
    return f_note("Tags: " + text) + "\n" + r" \normalsize" + "\n\n"


def attacks_latex(attacks: list) -> str:
    # for some reason they had "," replaced with "\n-" before... why?
    itemized_attacks = ""
    for attack in attacks:
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
    )


def skill_latex(
    field: list,
) -> str:
    return NoEscape(skipline + ("\n" + r" \medskip" + "\n").join(field))


def footer_latex(clean_name: str, encumbrance: str = ""):
    enc = f_note("Enc: " + encumbrance) if encumbrance else ""
    return rf""" \vfill
    {f_note(clean_name)} \hfill {enc}"""


def format_table_latex(table: ty.Table) -> str:
    text = (
        f"""\n\nRoll {table["roll"]} on this table.\n\n"""
        if "roll" in table.keys()
        else ""
    )
    text += NoEscape(
        r"""\smallskip\begin{center}
\begin{tabularx}{\textwidth}{ | c | X | }"""
    )
    for roll, outcome in table["outcomes"].items():
        text += NoEscape(
            rf"""
\hline
{roll} & {outcome} \\"""
        )
    text += NoEscape(
        r"""
    \hline
\end{tabularx}
\end{center}"""
    )
    return text


# latex entity text generation


def if_exists_format_latex(
    text: str | list = None,
    text_formatter: Callable = lambda text: text,
    field_text: str = "",
    field_text_formatter: Callable = lambda text: text,
    add_newline: bool = True,
    add_skipline: bool = False,
    hide: bool = False,
) -> str:
    if hide or not text:
        return ""
    text = text_formatter(text)
    text = text + " \n \n" if add_newline else text
    text = text + skipline if add_skipline else text
    if field_text:
        text = field_text_formatter(field_text + ":") + " " + text
    return text


formatting_dict_latex: dict[str, dict] = {
    "attacks": {"text_formatter": attacks_latex},
    "clean_name": {"hide": True},
    "cost": {
        "field_text": "Cost",
        "field_text_formatter": emph,
        "text_formatter": lambda x: ", ".join(x),
    },
    "effect": {},
    "encumbrance": {"hide": True},
    # need to put this and maybe encumbrance on the footer..
    "meta_tags": {"hide": True},
    "flavor_text": {"text_formatter": lambda text: skipline + italic(text)},
    "holds": {"field_text": "Holds", "field_text_formatter": emph},
    "hp": {"field_text": "HP", "field_text_formatter": emph},
    "name": {"text_formatter": lambda text: NoEscape(bold(large(text)))},
    "requirements": {
        "field_text": "Requirements",
        "field_text_formatter": emph,
        "text_formatter": lambda x: ", ".join(x),
    },
    "scores": {
        "field_text": "Scores",
        "field_text_formatter": emph,
        "text_formatter": lambda x: ", ".join(x),
    },
    "skills": {
        "field_text": "Skills",
        "field_text_formatter": emph,
        "text_formatter": skill_latex,
    },
    "speed": {"field_text": "Speed", "field_text_formatter": emph},
    "tags": {
        "field_text": "Tags",
        "field_text_formatter": emph,
        "text_formatter": lambda x: ", ".join(x),
    },
    "target": {
        "field_text": "Target",
        "field_text_formatter": emph,
    },
    "to_hit": {"field_text": "To-Hit", "field_text_formatter": emph},
    "full_text": {"hide": True},  # TODO: create full_text formatter for latex
    "table": {"text_formatter": format_table_latex},
}

# MARKDOWN


def if_exists_format_md(
    text: str | list,
    text_wrapper: str = "",
    text_formatter: Callable = lambda text: text,
    field_text: str = "",
    field_text_wrapper: str = "**",  # note that this one is the only one that doesnt default empty
    prefix: str = "",
    add_newline: bool = True,
    hide: bool = False,
) -> str:
    if hide or not text:
        return ""
    a_newline = "  \n" if add_newline else ""
    text = text_formatter(text)
    if field_text:
        text = field_text_wrapper + field_text + ":" + field_text_wrapper + " " + text
    elif prefix:
        text = prefix + text
    return text_wrapper + text + text_wrapper + a_newline


def format_table_md(table: ty.Table) -> str:
    md_table = (
        f"""  \n\nUnless otherwise specified, roll {table["roll"]} on this table."""
        + "\n\n| Roll | Outcome |  \n| --- | --- |"
    )
    for roll, outcome in table["outcomes"].items():
        md_table += "\n" + f"| {roll} | {outcome} |  "
    return md_table + "\n"


def format_full_text_md(entity: dict) -> str:
    if "full_text" in entity.keys():
        return entity["full_text"] + "  \n\n\n"
    else:
        return ""


formatting_dict_md: dict[str, dict] = {
    "attacks": {"text_formatter": lambda x: ", ".join(x)},
    "clean_name": {"hide": True},
    "cost": {"field_text": "Cost", "text_formatter": lambda x: ", ".join(x)},
    "effect": {},
    "encumbrance": {"field_text": "Encumbrance"},
    "flavor_text": {"text_wrapper": "*"},
    "holds": {"field_text": "Holds"},
    "hp": {"field_text": "HP"},
    "meta_tags": {"hide": True},
    "name": {"prefix": "#### "},
    "requirements": {
        "field_text": "Requirements",
        "text_formatter": lambda x: ", ".join(x),
    },
    "scores": {"field_text": "Scores", "text_formatter": lambda x: ", ".join(x)},
    "skills": {"field_text": "Skills", "text_formatter": lambda x: ", ".join(x)},
    "speed": {"field_text": "Speed"},
    "tags": {"field_text": "Tags", "text_formatter": lambda x: ", ".join(x)},
    "target": {"field_text": "Target"},
    "to_hit": {"field_text": "To-Hit"},
    "full_text": {"text_formatter": format_full_text_md},
    "table": {"text_formatter": format_table_md},
}
