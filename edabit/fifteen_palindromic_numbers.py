def generate_palindromes(limit: int) -> list:
    result = []
    for i in range(limit + 1):
        str_cast = str(i)
        if str_cast == str_cast[::-1]:
            result.append(int(str_cast))
    return [int(i) for i in result[-15:]]
