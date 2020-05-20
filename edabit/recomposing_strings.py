def recompose(string):
    groups = {c: 0 if c.lower() in 'aeiou' else 1 for c in string}
    stack = [string[0]]
    clusters = []

    for char in string[1:]:
        if groups[stack[-1]] == groups[char]:
            stack.append(char)
        else:
            clusters.append(''.join(stack[::-1]))
            stack = [char]

    clusters = ''.join(clusters + stack[::-1])
    
    return ''.join(' ' + c if c.isupper() else c for c in clusters).strip()
