# mealPlan_Agent
A small solver that fills lunch and dinner for seven days under a few rules.

## Problem Description
Planning meals for an entire week can be time-consuming and repetitive. People often end up choosing the same meals or spending too much time deciding what to cook. This project aims to simplify weekly meal planning by developing a solver that automatically generates a seven-day meal schedule while satisfying a set of predefined constraints.

## Problem Formulation

### Variables
- 14 total variables (7 days of lunch & dinner): Monday-Lunch, Monday-Dinner, Tuesday-Lunch, Tuesday-Dinner, Wednesday-Lunch, Wednesday-Dinner, Thursday-Lunch, Thursday-Dinner, Friday-Lunch, Friday-Dinner, Saturday-Lunch, Saturday-Dinner, Sunday-Lunch, Sunday-Dinner

### Domains
- Each variable can be assigned a recipe from the available recipe collection.
- Each recipe has nutritional tags (protein, vegetable, or both) and an associated cooking time.

### Constraints
- **Recipe variety:** No recipe appears more than once in any three consecutive days (for both mean) 
- **Nutritional coverage:** Each day has at least one protein tag and one vegetable tag across its two meals. 
- **Cooking time:** The total cooking time for all 14 meals must not exceed 300 minutes.

## Algorithms & Techniques

### Backtracking
Explores possible meal assignments.
 
### Minimum Remaining Values (MRV)
MRV picks the meal slot with the fewest remaining recipes first, avoiding dead ends.

### Forward checking
Forward checking removes a chosen recipe from the next two days as soon as it is placed.

### Greedy: Baseline
The greedy algorithm serves as a baseline for comparison. It moves through the week in order, assigning the first available recipe that satisfies the current constraints. Unlike backtracking, it does not reconsider previous assignments when it reaches a dead end.

## Evaluation Plan
|**Evaluation metric**|**Success criteria**|
|:--------------------|:-------------------|
|Valid weekly schedule|All 14 meals are assigned|
|Cooking time|Total is at most 300 minutes|
|Meal variety|No recipe repeats within three consecutive days|
|Protein coverage|Every day includes protein|
|Vegetable coverage|Every day includes vegetables|

## Risks and Limitations
- **Cooking-time feasibility:** If every recipe takes at least 22 minutes, the minimum possible total cooking time is 308 minutes. This exceeds the 300-minute limit, meaning a valid schedule is mathematically impossible under that assumption.
- **Recipe preparation accuracy:** Actual cooking times may exceed listed preparation times due to additional preparation, cooking mistakes, or differences in equipment.

## How to Run the Project
### Clone the repository
git clone https://github.com/Amwaterwall/mealPlan_Agent.git

# Navigate into the project
cd mealPlan_Agent

# Run the program
python .\eval.py

## Example Output

## Future Improvements
# Weekly Meal Plan
A small CSP solver that fills lunch and dinner for seven days under three rules: variety, daily tags, and a cook-time cap.

# Files
recipes.py — the recipe list (name, cook time, tags) as a pandas DataFrame.
csp.py — variables, domain, and the three constraints.
solve.py — greedy first-fit (baseline) and just plain backtracking for now.
eval.py — runs both solvers and prints the plans.

# Run
pip install pandas
python3 eval.py

Need Python 3.10 or later.
