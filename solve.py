
# Solvers: greedy first-fit (baseline) and plain backtracking.


from csp import add, domain, empty_assignment, is_consistent, variables


def greedy_first_fit():
    """Baseline. Walk the week in order. Assign the first legal recipe.
    Return None if a slot has no legal recipe left."""
    assignment = empty_assignment()

    for _, variable in variables().iterrows():
        day = variable["day"]
        meal = variable["meal"]

        assigned = False

        for _, recipe in domain().iterrows():
            if is_consistent(assignment, day, meal, recipe):
                assignment = add(assignment, day, meal, recipe)
                assigned = True
                break
        
        if not assigned:
            return None
    return assignment


def backtracking():
    """Plain backtracking. Variables in order, values in domain order."""
    
    all_variables = variables()
    recipes = domain()

    def search(assignment):
        if len(assignment) == len(all_variables):
            return assignment.copy()

        for _, variable in all_variables.iterrows():
            day = variable["day"]
            meal = variable["meal"]

            already_assigned = (
                (assignment["day"] == day) &
                (assignment["meal"] == meal)
            ).any()

            if not already_assigned:
                break
        for _, recipe in recipes.iterrows():
            if is_consistent(assignment, day, meal, recipe):
                new_assignment = add(
                    assignment, day, meal, recipe
                )
                result = search(new_assignment)

                if result is not None:
                    return result
        return None
    return search(empty_assignment())