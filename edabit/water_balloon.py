def pop(state):
    n = max(state)
    state[:n], state[n + 1:] = range(0, n), range(n - 1, -1, -1)
    return state