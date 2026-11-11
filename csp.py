# CSP structure: variables, domains, and the three constraints.
# Recipes and the assignment are pandas objects.


import pandas as pd

from recipes import RECIPES


DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MEALS = ["lunch", "dinner"]
COOK_CAP = 300


def variables():
    # One row per (day, meal).
    # TODO: build a DataFrame with columns ["day", "meal"] for all 14 slots.
    return pd.DataFrame(columns=["day", "meal"])


def domain():
    # Every variable draws from the same recipe table.
    return RECIPES


def empty_assignment():
    # A plan starts empty.
    return pd.DataFrame(columns=["day", "meal", "name", "minutes", "tags"])


def no_repeat_ok(assignment, day, name):
    # No recipe appears more than once in any three consecutive days.
    # TODO: look at the two days before `day` (and today) and return False
    # if `name` is already used in that window.
    return True


def day_tags_ok(assignment, day, meal, tags):
    # Once both meals of a day are set, the day needs protein and vegetable.
    # TODO: if the other meal of this day is already assigned, combine the
    # tag sets and return True only if both "protein" and "vegetable" are present.
    return True


def cook_time_ok(assignment, minutes):
    # Running total of cook time stays under the cap.
    # TODO: return True if the current total plus `minutes` is <= COOK_CAP.
    return True


def is_consistent(assignment, day, meal, recipe):
    return (no_repeat_ok(assignment, day, recipe["name"])
            and day_tags_ok(assignment, day, meal, recipe["tags"])
            and cook_time_ok(assignment, recipe["minutes"]))


def add(assignment, day, meal, recipe):
    # Return a new assignment with this meal appended.
    # TODO: append one row (day, meal, name, minutes, tags) and return the new frame.
    return assignment