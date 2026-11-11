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

if __name__ == "__main__":
    print("Show plans...")