def compare_diagonal(matrix):
    left_diagonal = [matrix[i][i] for i in range(len(matrix))]
    right_diagonal = [matrix[::-1][i][i] for i in range(len(matrix[::-1]))]
    return right_diagonal[::-1] if sum(right_diagonal) >= sum(left_diagonal) else left_diagonal