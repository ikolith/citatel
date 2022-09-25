import itertools
import re
import random


def all_rolls(dice: list, result_type: str = "all") -> dict:
    """Pass in a list where each die is represented by an integer corresponding to its maximum value.
    Returns a dictionary where keys are the totals (or result) of the rolls.
    The values are dependent on result_type.
    If 'all', all possible combinations that resulted in that roll.
    If 'count' a count of how many distinct combinations there are.
    If 'probabilities', the probability of the result."""
    dice_ranges = [range(1, die + 1) for die in dice]
    all_rolls = {}

    for i in itertools.product(*dice_ranges):
        if sum(i) in all_rolls.keys():
            all_rolls[sum(i)].append(i)
        else:
            all_rolls[sum(i)] = [i]

    if result_type == "all":
        return all_rolls
    elif result_type == "counts":
        return {i: len(all_rolls[i]) for i in all_rolls}
    elif result_type == "probabilities":
        roll_counts = {i: len(all_rolls[i]) for i in all_rolls}
        return {i: roll_counts[i] / sum(roll_counts.values()) for i in roll_counts}
    else:
        raise Exception("Invalid result_type passed.")


def get_ev(dice: list, mod="") -> float:
    if mod == "":
        return float(sum(dice) / len(dice) + (len(dice) * 0.5))
    elif mod == "double_on_max":
        return float(sum(dice) / len(dice) + (len(dice) * 0.5) + len(dice))
    elif mod == "exploding":
        ev = 0
        for die in dice:
            ev += (die * (die + 1)) / (2 * (die - 1))
        return float(ev)
    else:
        raise Exception("Invalid modifier (mod) argument passed.")


def get_cumulative_probability(roll_probabilities: dict) -> dict:
    cum_prob = {}
    run_sum = 0
    for roll in roll_probabilities:
        run_sum += roll_probabilities[roll]
        cum_prob[roll] = run_sum
    return cum_prob


def score_adjustment(roll_df: dict, adjustment: int) -> dict:
    return {roll + adjustment: v for roll, v in roll_df.items()}


# I feel like this is going to be used often enough that I might as well keep this around.
std_check_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def get_pass_probability(score: int, dc: int) -> float:
    cum_prob = score_adjustment(
        get_cumulative_probability(std_check_probabilities), score
    )
    if max(cum_prob.keys()) < dc - 1:
        return 0.0
    elif min(cum_prob.keys()) > dc - 1:
        return 1.0
    else:
        return 1 - cum_prob[dc - 1]


def die_parser_roller(curly_match: str) -> int:
    quantity, top_face, x, mod = re.search(
        r"(\d*)d(\d+)(x?)([-+]?\d*)", curly_match
    ).groups()
    assert top_face
    top_face = int(top_face)
    if not quantity:
        quantity = 1
    else:
        quantity = int(quantity)
    roll = 0
    for i in range(0, quantity):
        just_rolled = random.randint(1, top_face)
        if x and top_face > 1:
            while just_rolled == top_face:
                roll += just_rolled
                just_rolled = random.randint(1, top_face)
        roll += just_rolled
    if not mod:
        pass
    else:
        roll += int(mod)
    return max(
        roll, 0
    )  # Here following the ttrpg convention that you cannot roll a negative number.
