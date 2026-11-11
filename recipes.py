"""Recipes for the meal-plan CSP, stored as a pandas DataFrame."""

import pandas as pd


RECIPES = pd.DataFrame([
    {"name": "chicken rice",  "minutes": 25, "tags": {"protein"}},
    {"name": "tofu stir-fry", "minutes": 20, "tags": {"protein", "vegetable"}},
    {"name": "pasta",         "minutes": 30, "tags": {"protein"}},
    {"name": "salad",         "minutes": 10, "tags": {"vegetable"}},
    {"name": "soup",          "minutes": 35, "tags": {"vegetable"}},
    {"name": "omelette",      "minutes": 15, "tags": {"protein"}},
    {"name": "bean tacos",    "minutes": 20, "tags": {"protein", "vegetable"}},
    {"name": "grilled fish",  "minutes": 25, "tags": {"protein"}},
    {"name": "veggie bowl",   "minutes": 15, "tags": {"vegetable"}},
    {"name": "fried rice",    "minutes": 20, "tags": {"protein", "vegetable"}},
    {"name": "lentil stew",   "minutes": 40, "tags": {"protein", "vegetable"}},
    {"name": "caprese",       "minutes": 10, "tags": {"vegetable"}},
])