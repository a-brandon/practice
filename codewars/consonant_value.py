def solve(s):
    cons = ''.join(x if x not in 'aeiou' else ' ' for x in s).split()

    for i, ch in enumerate(cons):
        total = 0
        if len(ch) > 1:
            for c in ch:
                total += ord(c) - 96
        else:
            total += ord(ch) - 96
        cons[i] = total

    return max(cons)



print(solve('zodiacs'))