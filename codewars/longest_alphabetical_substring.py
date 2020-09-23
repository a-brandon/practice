def longest(s):
    prev, longest_sub = s[0], []

    for letter in s[1:]:
        if ord(letter) >= ord(prev[-1]):
            prev += letter
        else:
            longest_sub.append(prev)
            prev = letter
    longest_sub.append(prev)

    return max(longest_sub, key=len)