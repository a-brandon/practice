def printgrid(rows, cols):
    return [[*range(i, (rows * cols + 1), rows)] for i in range(1, rows + 1)]
