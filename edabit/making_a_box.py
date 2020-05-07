def makeBox(n):
    return ['#' * n if i in {0, n-1} else '#' + ' ' * (n - 2) + '#' for i in range(n)]
