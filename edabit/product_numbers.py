def get_products(lst):
    result = []
    pos = 0
    prod = 1
    count = 0
    while pos < len(lst):
        for i, num in enumerate(lst):
            if i != pos:
                prod *= num
                count += 1
            if count == len(lst) - 1:
                result.append(prod)
                prod = 1
                pos += 1
                count = 0
    return result
