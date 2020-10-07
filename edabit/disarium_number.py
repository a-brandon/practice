def is_disarium(n):
    return sum(int(num) ** i for i, num in enumerate(str(n), start=1)) == n