"""Recipes for the meal-plan CSP. Each recipe has a name, a cook time, and tags."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Set


@dataclass
class Recipe:
    name: str
    minutes: int
    tags: Set[str]


# Twelve recipes. Enough variety for a 7-day week under the 3-day no-repeat rule.
RECIPES = [
    Recipe("chicken rice",   25, {"protein"}),
    Recipe("tofu stir-fry",  20, {"protein", "vegetable"}),
    Recipe("pasta",          30, {"protein"}),
    Recipe("salad",          10, {"vegetable"}),
    Recipe("soup",           35, {"vegetable"}),
    Recipe("omelette",       15, {"protein"}),
    Recipe("bean bowl",      20, {"protein", "vegetable"}),
    Recipe("fish tacos",     25, {"protein"}),
    Recipe("veggie wrap",    15, {"vegetable"}),
    Recipe("fried rice",     20, {"protein", "vegetable"}),
    Recipe("lentil stew",    40, {"protein", "vegetable"}),
    Recipe("grilled cheese", 10, {"protein"}),
]