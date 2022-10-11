import pandas as pd
from pylatex.utils import NoEscape
import py_utils.vars as v
import os

# single entity text generators. used for cli and various utilities.


def if_field_exists_md(text: str, field_text: str = "") -> str:
    return field_md(field_text) + " " + text if text else ""


def field_md(field_text: str) -> str:
    return f"**{field_text}**" if field_text else ""


def name_md(text: str) -> str:
    return f"""### {text}"""


def flavor_md(text: str) -> str:
    return "*" + text + "*" if text else ""


def generate_weapon_md(row: pd.Series) -> str:
    row["basic_attacks"] = row["basic_attacks"].replace(",", "\n-")
    return f"""{name_md(row['name'])}  
{if_field_exists_md(row['tags'],'Tags:')}  
{if_field_exists_md(row['requirements'], 'Requirements:')}    
{if_field_exists_md(row['speed'], "Speed:")}, {if_field_exists_md(row['to_hit'],"To Hit:")} 
- {row['basic_attacks']}  

{if_field_exists_md(row['effect'])}  

{if_field_exists_md(flavor_md(row['flavor_text']))}""".strip()


def generate_invocation_md(row: pd.Series) -> str:
    return f"""{name_md(row['name'])}  
{if_field_exists_md(row['target'],"Target:")}    
{row['effect']}  
  
{if_field_exists_md(flavor_md(row['flavor_text']))}""".strip()


def generate_item_md(row: pd.Series) -> str:
    return f"""{name_md(row['name'])}  
{row['effect']}  
  
{if_field_exists_md(flavor_md(row['flavor_text']))}""".strip()


def generate_npc_md(row: pd.Series) -> str:
    row["skills"] = row["skills"].replace(",", "\n-")
    return f"""{name_md(row['name'])}  
{if_field_exists_md(row['hp'],"HP:")}  
{if_field_exists_md(row['scores'],"Scores:")}    
{if_field_exists_md(row['skills'],"Skills:")}  
{if_field_exists_md(row['holds'], "Holds:")}  
  
{flavor_md(row['flavor_text'])}""".strip()


def generate_skill_md(row: pd.Series) -> str:
    return f"""{name_md(row['name'])}  
{if_field_exists_md(row["requirements"],"Requirements:")}  
{if_field_exists_md(row["cost"],"Cost:")}    
{(row["effect"])}""".strip()


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
    newline = "\n" + "\n" if end_with_newline else ""
    field_text = emph(field_text) if field_text else ""
    if text:
        return field_text + text + newline
    else:
        return ""


def if_exists(text: str) -> str:
    return text if text else ""


def name_latex(text: str) -> str:
    return bold(large(text)) + "\n\n"


def line_section_if_exists_latex(text: str, use_italics: bool = True) -> str:
    text = italic(text) if use_italics and text else text
    return skipline + text if text else ""


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
        + line_section_if_exists_latex(row["flavor_text"])
        + footer_latex(row["clean_name"])
    )


def generate_item_latex(row: pd.Series) -> str:
    return NoEscape(
        name_latex(row["name"])
        + row["effect"]
        + line_section_if_exists_latex(row["flavor_text"])
        + footer_latex(row["clean_name"], row["encumbrance"])
    )


def generate_npc_latex(row: pd.Series) -> str:
    return NoEscape(
        name_latex(row["name"])
        + if_field_exists_latex(row["hp"], "HP: ")
        + if_field_exists_latex(row["scores"], "Scores: ")
        + if_field_exists_latex(row["skills"], "Skills: ")
        + if_field_exists_latex(row["holds"], "Holds: ", False)
        + if_field_exists_latex(line_section_if_exists_latex(row["flavor_text"]))
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
        + line_section_if_exists_latex(row["flavor_text"])
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


# the entity text generator


def generate_entity_text(
    entity_type: str,
    row: pd.Series,
    text_type: str = "md",
    html_characters: bool = False,
) -> str:
    if text_type == "md":
        if html_characters:
            # these are all in some html version??
            arrow = "&#8658;"
            empty_triangle_r = "&#9655;"
            filled_triangle_r = "&#9654;"
            triangle_up = "&#9650;"
            row = row.str.replace(
                r"[_]", r"\_", regex=True
            )  # not sure if md needs this but probably does!
            row = row.str.replace(r"->", f"{arrow}", regex=True)
            # replacing text with latex glyphs for the [swinging: ...], [thrusting] tags
            row = row.str.replace(
                r"\[swinging: following]",
                f"{filled_triangle_r} {empty_triangle_r} {empty_triangle_r}",
                regex=True,
            )
            row = row.str.replace(
                r"\[swinging: neutral]",
                f"{empty_triangle_r} {filled_triangle_r} {empty_triangle_r}",
                regex=True,
            )
            row = row.str.replace(
                r"\[swinging: leading]",
                f"{empty_triangle_r} {empty_triangle_r} {filled_triangle_r}",
                regex=True,
            )
            row = row.str.replace(
                r"\[thrusting]",
                f"{triangle_up}",
                regex=True,
            )

        if entity_type == "armors":
            pass  # dont have csvs for armor yet
        elif entity_type == "invocations":
            text = generate_invocation_md(row)
        elif entity_type == "items":
            text = generate_item_md(row)
        elif entity_type == "npcs":
            text = generate_npc_md(row)
        elif entity_type == "weapons":
            text = generate_weapon_md(row)
        elif entity_type == "skills":
            text = generate_skill_md(row)
        else:
            raise Exception("Unsupported entity type.")
    if text_type == "latex":
        row = row.str.replace(r"[{}]", "", regex=True)
        row = row.str.replace(r"[_]", r"\_", regex=True)
        row = row.str.replace(r"->", "$\\\Rightarrow$", regex=True)
        # replacing text with latex glyphs for the [swinging: ...], [thrusting] tags
        row = row.str.replace(
            r"\[swinging: following]",
            r"$\\blacktriangleright\\mkern-7mu\\triangleright\\mkern-7mu\\triangleright$",
            regex=True,
        )
        row = row.str.replace(
            r"\[swinging: neutral]",
            r"$\\triangleright\\mkern-7mu\\blacktriangleright\\mkern-7mu\\triangleright$",
            regex=True,
        )
        row = row.str.replace(
            r"\[swinging: leading]",
            r"$\\triangleright\\mkern-7mu\\triangleright\\mkern-7mu\\blacktriangleright$",
            regex=True,
        )
        row = row.str.replace(
            r"\[thrusting]",
            r"$\\blacktriangle$",
            regex=True,
        )
        if entity_type == "armors":
            pass  # dont have csvs for armor yet
        elif entity_type == "invocations":
            text = generate_invocation_latex(row)
        elif entity_type == "items":
            text = generate_item_latex(row)
        elif entity_type == "npcs":
            text = generate_npc_latex(row)
        elif entity_type == "weapons":
            text = generate_weapon_latex(row)
        elif entity_type == "skills":
            text = generate_skill_latex(row)
        else:
            raise Exception("Unsupported entity type.")
    return text


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
