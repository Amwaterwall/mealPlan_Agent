
# Solvers: greedy first-fit (baseline) and plain backtracking.


from csp import add, domain, empty_assignment, is_consistent, variables


def greedy_first_fit():
    """Baseline. Walk the week in order. Assign the first legal recipe.
    Return None if a slot has no legal recipe left."""
    # TODO:
    #   assignment = empty_assignment()
    #   for each (day, meal) in variables():
    #       try each recipe in domain()
    #       if is_consistent(...): assignment = add(...); break
    #       if none fit: return None
    #   return assignment
    return None


def backtracking():
    """Plain backtracking. Variables in order, values in domain order.
    MRV and forward checking come later."""
    # TODO:
    #   def search(assignment):
    #       if every variable is assigned: return a copy
    #       pick the first unassigned (day, meal)
    #       for each recipe in domain():
    #           if is_consistent: recurse on add(...)
    #           if the result is not None: return it
    #       return None
    #   return search(empty_assignment())
    return None