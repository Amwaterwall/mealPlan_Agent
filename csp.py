"""CSP structure: variables, domains, and the three constraints."""

from __future__ import annotations
from typing import Dict, List, Tuple

from recipes import RECIPES, Recipe


DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MEALS = ["lunch", "dinner"]
COOK_CAP = 300          