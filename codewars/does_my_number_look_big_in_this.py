def narcissistic(value):
    return sum(int(x) ** int(len(str(value))) for x in str(value)) == value