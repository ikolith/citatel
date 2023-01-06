from pylatex.utils import NoEscape
import citutils.my_types as ty
import citutils.commands as co
import os
from collections.abc import Callable
from copy import deepcopy
import re

# single entity text generators. used for cli and various utilities.

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

# latex section formatting


def tag_latex(
    text: str,
) -> str:
    # havent gotten rid of this one because im not decided on whether ill use it, not using it for now
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


def skill_effect_latex(
    text: str,
) -> str:
    # TODO: entities still have that fucking :: in them... need to get rid of that and adjust this function
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


def if_exists_format_latex(
    text: str = "",
    text_formatter: Callable = lambda text: text,
    field_text: str = "",
    field_text_formatter: Callable = lambda text: text,
    add_newline: bool = True,
    add_skipline: bool = False,
    hide: bool = False,
) -> str:
    if hide or not text:
        return ""
    if_newline = " \n \n" if add_newline else ""
    if_skipline = skipline if add_skipline else ""
    if field_text:
        return (
            field_text_formatter(field_text + ":")
            + " "
            + text
            + if_skipline
            + if_newline
        )
    return text_formatter(text) + if_skipline + if_newline


formatting_dict_latex: dict[str, dict] = {
    "basic_attacks": {"text_formatter": attacks_latex},
    "cost": {"field_text": "Cost", "field_text_formatter": emph},
    "effect": {"text_formatter": skill_effect_latex},
    "encumbrance": {"hide": True},
    # need to put this and maybe encumbrance on the footer..
    "filter_tags": {"hide": True},
    "flavor_text": {"text_formatter": lambda text: skipline + italic(text)},
    "holds": {"field_text": "Holds", "field_text_formatter": emph},
    "hp": {"field_text": "HP", "field_text_formatter": emph},
    "name": {"text_formatter": lambda text: NoEscape(bold(large(text)))},
    "requirements": {"field_text": "Requirements", "field_text_formatter": emph},
    "scores": {"field_text": "Scores", "field_text_formatter": emph},
    "skills": {
        "field_text": "Skills",
        "field_text_formatter": emph,
        "text_formatter": skill_effect_latex,
    },
    "speed": {"field_text": "Speed", "field_text_formatter": emph},
    "tags": {"field_text": "Tags", "field_text_formatter": emph},
    "target": {
        "field_text": "Target",
        "field_text_formatter": emph,
    },
    "to_hit": {"field_text": "To-Hit", "field_text_formatter": emph},
    "full_text": {"hide": True},
}


def generate_latex(
    entity: dict,
    formatting: dict[str, dict] = formatting_dict_latex,
    footer: bool = True,
) -> str:
    result_text = ""
    for key, text in entity.items():
        result_text += if_exists_format_latex(
            text=str(text), **formatting_dict_latex[key]
        )
    if footer and "encumbrance" in entity.keys():
        filter_tags = entity["filter_tags"] if "filter_tags" in entity.keys() else ""
        result_text += rf"""\vfill
        {filter_tags} \hfill {"Enc: " + entity["encumbrance"]} 
        """  # this used to include clean name before the \hfill (so on the left side) and i dont really think thats necessary anymore ... though maybe filter_tags would be nice still
    return result_text


# md generation


def if_exists_format_md(
    text: str,
    text_wrapper: str = "",
    prefix: str = "",
    field_text: str = "",
    field_wrapper: str = "**",  # note that this one is the only one that doesnt default empty
    newline: bool = True,
    hide: bool = False,
) -> str:
    if hide:
        return ""
    a_newline = "  \n" if newline else ""
    if field_text:
        return field_wrapper + field_text + ":" + field_wrapper + " " + text + a_newline
    elif prefix:
        return prefix + " " + text + a_newline
    return text_wrapper + text + text_wrapper + a_newline


formatting_dict_md: dict[str, dict] = {
    "basic_attacks": {},
    "cost": {"field_text": "Cost"},
    "effect": {},
    "encumbrance": {"field_text": "Encumbrance"},
    "filter_tags": {"hide": True},
    "flavor_text": {"text_wrapper": "*"},
    "holds": {"field_text": "Holds"},
    "hp": {"field_text": "HP"},
    "name": {"prefix": "#### "},
    "requirements": {"field_text": "Requirements"},
    "scores": {"field_text": "Scores"},
    "skills": {"field_text": "Skills"},
    "speed": {"field_text": "Speed"},
    "tags": {"field_text": "Tags"},
    "target": {"field_text": "Target"},
    "to_hit": {"field_text": "To-Hit"},
    "full_text": {
        "hide": True
    },  # generate_full_text_md() handles this instead of generate_md()
}


def generate_md(
    entity: dict,
    formatting: dict = formatting_dict_md,
) -> str:
    result_text = ""
    for key, text in entity.items():
        result_text += if_exists_format_md(text=str(text), **formatting[key])
    return result_text


def generate_full_text_md(entity: dict) -> str:
    # not sure how i want this to be built in yet, so its a different step..
    # TODO: come back after building and review the setup here
    if "full_text" in entity.keys():
        return entity["full_text"] + "  \n\n\n"
    else:
        return ""


def generate_entity_text(
    entity: ty.Entity,
    text_type: str = "md",
    html_characters: bool = False,
    include_full_text: bool = False,  # only used by .md right now..
    skip_generation: bool = False  # only used by .md right now!
    # TODO: maybe look into pushing latex book generation up forward a bit
    # stuff keeps getting built that only works for .md, latex really is just for cards atm
    # TODO: this doesn't show up in the curly command and probably it should! and maybe some other ones too
) -> str:
    entity_local = deepcopy(entity)
    if text_type == "md":
        if html_characters:
            arrow = "&#8658;"
            empty_triangle_r = "&#9655;"
            filled_triangle_r = "&#9654;"
            triangle_up = "&#9650;"
            for key in entity_local.keys():  # untested.. yet
                entity_local[key] = re.sub(r"[_]", r"\_", entity_local[key])
                entity_local[key] = re.sub(r"->", f"{arrow}", entity_local[key])
                entity_local[key] = re.sub(
                    r"\[swinging: following]",
                    f"{filled_triangle_r} {empty_triangle_r} {empty_triangle_r}",
                    entity_local[key],
                )
                entity_local[key] = re.sub(
                    r"\[swinging: neutral]",
                    f"{empty_triangle_r} {filled_triangle_r} {empty_triangle_r}",
                    entity_local[key],
                )
                entity_local[key] = re.sub(
                    r"\[swinging: leading]",
                    f"{empty_triangle_r} {empty_triangle_r} {filled_triangle_r}",
                    entity_local[key],
                )
                entity_local[key] = re.sub(
                    r"\[thrusting]",
                    f"{triangle_up}",
                    entity_local[key],
                )
        md_text = generate_md(entity_local) if not skip_generation else ""
        if include_full_text:
            md_text = generate_full_text_md(entity_local) + md_text + "  \n\n"
        return md_text
    elif text_type == "latex":
        if "basic_attacks" in entity_local.keys():
            entity_local["basic_attacks"] = re.sub(
                r",", r"\n-", entity_local["basic_attacks"]
            )
        for key in entity_local.keys():
            entity_local[key] = re.sub(r"[{}]", "", entity_local[key])
            entity_local[key] = re.sub(r"([a-z0-9])(_)", r"\1\_", entity_local[key])
            entity_local[key] = re.sub(r"->", "$\\\Rightarrow$", entity_local[key])
            # replacing text with latex glyphs for the [swinging: ...], [thrusting] tags
            entity_local[key] = re.sub(
                r"\[swinging\: following]",
                r"$\\blacktriangleright\\mkern-7mu\\triangleright\\mkern-7mu\\triangleright$",
                entity_local[key],
            )
            entity_local[key] = re.sub(
                r"\[swinging\: neutral]",
                r"$\\triangleright\\mkern-7mu\\blacktriangleright\\mkern-7mu\\triangleright$",
                entity_local[key],
            )
            entity_local[key] = re.sub(
                r"\[swinging\: leading]",
                r"$\\triangleright\\mkern-7mu\\triangleright\\mkern-7mu\\blacktriangleright$",
                entity_local[key],
            )
            entity_local[key] = re.sub(
                r"\[thrusting]",
                r"$\\blacktriangle$",
                entity_local[key],
            )
        return generate_latex(entity_local)
    else:
        raise Exception("text_type needs to be either 'latex' or 'md'.")


def filter_generate_text(  # this is called "text" not "md"... and the params suggest it would work okay with latex, but im not sure thats actually true.
    entities: ty.Entities,
    filter_tags_include: str = "",
    filter_tags_exclude: str = "",
    include_full_text: bool = False,
    text_type: str = "md",
    html_characters: bool = False,
    skip_generation: bool = False,
) -> str:
    if text_type == "md":
        text = ""
        filtered_entities = co.filter_entities_by_filter_tags(
            entities, filter_tags_include, filter_tags_exclude
        )
        for entity in filtered_entities.values():
            text += (
                generate_entity_text(
                    entity,
                    text_type,
                    html_characters,
                    include_full_text,
                    skip_generation,
                )
                + "  \n\n"
            )
        return text
    else:
        raise Exception("text_type needs to be 'md'. Only 'md' is supported right now.")


def generate_doc_text(  # this is called "text" not "md"... and the params suggest it would work okay with latex, but im not sure thats actually true.
    entities: ty.Entities,
    entity_sections: ty.ESs,
    front_text: str = "",
    end_text: str = "",
    text_type: str = "md",
    html_characters: bool = False,
    skip_generation: bool = False,
) -> str:
    """DEPRECATED: not really necessary given quarto"""
    if text_type == "md":
        doc = front_text
        for section in entity_sections:
            if "include_full_text" not in section.keys():
                include_full_text = False
            else:
                include_full_text = section["include_full_text"]
            if "text" in section.keys():
                doc += section["text"] + "  \n\n"
            if "clean_name" in section.keys():
                doc += generate_entity_text(
                    entities[section["clean_name"]],
                    text_type,
                    html_characters,
                    include_full_text,
                    skip_generation,
                )
                continue
            fi, fx = "", ""
            if "fi" in section.keys():
                fi = section["fi"]
            if "fx" in section.keys():
                fx = section["fx"]
            filtered_entities = co.filter_entities_by_filter_tags(entities, fi, fx)
            for entity in filtered_entities.values():
                doc += (
                    generate_entity_text(
                        entity,
                        text_type,
                        html_characters,
                        include_full_text,
                        skip_generation,
                    )
                    + "  \n\n"
                )
        return doc + end_text
    else:
        raise Exception("text_type needs to be 'md'. Only 'md' is supported right now.")
