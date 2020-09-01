def get_luckiest(list_of_numbers):
    if not list_of_numbers:
        return None

    fives = {n: n.count('5') for n in list(map(str, list_of_numbers))}

    if all(fives.get(num) == 0 for num in fives):
        return list_of_numbers[0]

    return sorted(int(f) for f in fives if fives[f] == max(fives.values()))[-1]