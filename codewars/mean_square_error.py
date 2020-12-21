def solution(array_a, array_b):
    return sum(abs(x - y) ** 2 for x, y in zip(array_a, array_b)) / len(array_a)