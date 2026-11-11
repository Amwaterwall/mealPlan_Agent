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