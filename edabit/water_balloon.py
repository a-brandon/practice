def pop(state):
    if state == [0]:
        return state
    balloon = state
    pop_idx = next(i for i in state if i)
    balloon[1:pop_idx] = [i for i in range(1, pop_idx)]
    balloon[pop_idx + 1:-1] = [i for i in range(pop_idx - 1, 0, -1)]
    return balloon
