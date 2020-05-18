def is_match(open_sym, close_sym):
    parens = {'[': ']', '{': '}', '(': ')'}
    return parens[open_sym] == close_sym


def isBalanced(txt):
    if txt is None:
        return 

    stack = []
    i, balanced = 0, True

    while i < len(txt) and balanced:
        curr_symbol = txt[i]
        if curr_symbol in '[{(':
            stack.append(curr_symbol)
        elif not stack:
            balanced = False
        else:
            open_sym = stack.pop()
            if not is_match(open_sym, curr_symbol):
                balanced = False
        i += 1

    return True if not stack and balanced else False
