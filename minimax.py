# No mini

from numba import njit

g = game.Game()

@njit
def minimax_no_mini(g, depth, alpha, beta):
    if depth >= 2:
        return g.get_score()

    maxEval = float("-inf")
    for i in range(7):
        for j in range(7):
            for k in range(4):
                clone = g.copy()
                clone.move(i, j, k)
                ret = minimax_no_mini(clone, depth + 1, alpha, beta)
                maxEval = max(maxEval, ret)
                alpha = max(alpha, ret)
                if beta <= alpha:
                    break
            else:
                continue
            break
        else:
            continue
        break

    return maxEval

print(minimax_no_mini(g, 0, float("-inf"), float("inf")))