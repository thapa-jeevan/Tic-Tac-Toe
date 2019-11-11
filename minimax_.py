from math import inf as inf


def maximize_(state, alpha, beta, cost):
    terminal_value = state.is_terminal()
    if terminal_value is not False:
        return None, terminal_value, cost

    intermediate_cost = inf
    max_child_action, max_score = None, -inf
    for cell in state.empty_cells():
        clone = state.clone_and_move(cell, 1)
        _, score, terminal_cost = minimize_(clone, alpha, beta, cost + 1)

        if score > max_score:
            if terminal_cost < intermediate_cost:
                max_score = score
                max_child_action = cell
                intermediate_cost = terminal_cost

        if max_score >= beta:
            break

        if max_score > alpha:
            alpha = max_score

    return max_child_action, max_score, intermediate_cost


def minimize_(state, alpha, beta, cost):
    terminal_value = state.is_terminal()
    if terminal_value is not False:
        return None, terminal_value, cost

    intermediate_cost = inf
    min_child_action, min_score = None, inf
    for cell in state.empty_cells():
        clone = state.clone_and_move(cell, -1)

        _, score, terminal_cost = maximize_(clone, alpha, beta, cost + 1)

        if score < min_score:
            if terminal_cost < intermediate_cost:
                min_score = score
                min_child_action = cell
                intermediate_cost = terminal_cost

        if min_score <= alpha:
            break

        if min_score < beta:
            beta = min_score
    return min_child_action, min_score, intermediate_cost
