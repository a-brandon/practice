def order_weight(strng):
    return ' '.join(sorted(sorted(strng.strip().split()), key=lambda n: sum(int(i) for i in n)))