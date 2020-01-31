def checkio(data: list) -> list:
    non_unique = []
    for num in data:
        if data.count(num) >= 2:
            non_unique.append(num)
    return non_unique
