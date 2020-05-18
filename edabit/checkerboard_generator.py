def checker_board(n, e1, e2):
    if e1 == e2:
        return 'invalid'
    return [([e1, e2] * n)[:n] if not i % 2 else ([e1, e2] * n)[::-1][:n] for i in range(n)]
