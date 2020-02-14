def generate_palindromes(limit):
    return sorted(i for i in range(limit + 1) if str(i) == str(i)[::-1])[-15:]
