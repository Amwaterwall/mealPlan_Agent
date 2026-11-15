# Run both solvers and print the plans.

from csp import COOK_CAP, variables
from solve import backtracking, greedy_first_fit

# TODO: write a show(title, plan) function that:
#   - prints "no plan found" if plan is None or empty
#   - otherwise walks variables() in order and prints day, meal, name, minutes, tags
#   - prints the total cook time and the cap
def show(title, plan):
    """Print one plan in week order, or say that none was found.

    title  -- label for the solver ("Greedy first-fit", "Backtracking")
    plan   -- DataFrame of assigned meals, or None if the solver failed
    """
    print(f"\n{title}")

    # A failed solver returns None. An empty frame is also a failure.
    if plan is None or len(plan) == 0:
        print("  no plan found")
        return

    # Total cook time is the sum of the minutes column.
    total = int(plan["minutes"].sum())

    # Walk the variables in week order so the printout is Mon-lunch first
    for _, var in variables().iterrows():
        rows = plan[(plan["day"] == var["day"]) & (plan["meal"] == var["meal"])]
        if rows.empty:
            continue
        row = rows.iloc[0]
        tags = sorted(row["tags"])
        print(f"  {row['day']:3s} {row['meal']:7s}  {row['name']:16s}  "
              f"{int(row['minutes']):3d} min  {tags}")

    print(f"  total cook time: {total} min  (cap {COOK_CAP})")

if __name__ == "__main__":
    # Baseline first, then the search, compare side by side.
    show("Greedy first-fit (baseline)", greedy_first_fit())
    show("Backtracking", backtracking())