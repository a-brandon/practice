palindrome = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i * j) == str(i * j)[::-1]:
            palindrome.append(i * j)
m = max(palindrome)
