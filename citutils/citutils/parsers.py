import re

import citutils.dice_utils as du
import citutils.text_generators as ge
import citutils.my_types as ty


def get_clean_name(name: str) -> str:
    """Returns a name in lowercase with numbers left alone, whitespace stripped, " " and "-" replaced with "_", and every other character removed."""
    return re.sub(
        r"[^a-z0-9_]", "", name.lower().strip().replace(" ", "_").replace("-", "_")
    )


def parse_curlies(text: str) -> list[ty.Curly]:
    curlies = re.findall(r"{[^}]*}", text)
    dice_pattern = r"\d*?d\d+x?[+-]?\d*"
    curlies_parsed = []
    if curlies:
        for match in curlies:
            # Check for entity...
            quantity = 1
            if (e := re.search(r"(?<=\s|{)([a-zA-Z_',;:\-()\s]+)", match)) is not None:
                entity = get_clean_name(e.group())
            else:
                entity = ""
            # Check for quantity dice (leading dice)...
            if q := re.search(rf"(?<={{){dice_pattern}", match):
                quantity_dice = q.group()
                quantity = du.die_parser_roller(quantity_dice)
            # Check for number
            else:
                if entity == "":
                    continue
                elif (n := re.search(r"(?<={)\d+(?=\s)", match)) is not None:
                    quantity_dice = ""
                    quantity = int(n.group())
                else:
                    quantity_dice = ""
            if entity and (t := re.search(rf"({dice_pattern})(?=}})", match)):
                table_dice = t.group()
                table_result = du.die_parser_roller(table_dice)
            elif entity and (t := re.search(r"(\d+)(?=})", match)):
                table_dice = ""
                table_result = int(t.group())
            else:
                table_dice = ""
                table_result = None
            curlies_parsed.append(
                ty.Curly(
                    {
                        "match": match,
                        "quantity_dice": quantity_dice,
                        "table_dice": table_dice,
                        "entity": entity,
                        "quantity": quantity,
                        "table_result": table_result,
                    }
                )
            )
    return curlies_parsed


def single_curly_parser(
    db,
    text: str,
    expand_entities: bool = False,
    roll_dice: bool = False,
) -> str:
    if not (text.startswith("{") and text.endswith("}")):
        text = "{" + text + "}"
    curlies_parsed = parse_curlies(text)
    assert len(curlies_parsed) == 1
    base_curly = curlies_parsed[0]
    # case when only die roll is present
    if not base_curly["entity"]:
        return str(du.die_parser_roller(base_curly["quantity_result"]))
    # all other cases
    return ge.generate_entity_tree_text(db, base_curly, expand_entities, roll_dice)
