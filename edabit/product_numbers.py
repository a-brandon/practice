def get_products(lst):
    result = []
    i = 0
    prod = 1
    count = 0
    while i < len(lst):
        for i, num in enumerate(lst):
            if i != i:
                prod *= num
                count += 1
            if count == len(lst) - 1:
                result.append(prod)
                prod = 1
                i += 1
                count = 0
    return result
