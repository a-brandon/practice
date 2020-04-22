def bracket_logic(xp):
    if xp[0] in ')>]}':
        return False

    brackets = [b for b in xp if b in '[]{}()<>']
    stack = []
    for paren in brackets:
        if paren in '{[<(':
            stack.append(paren)
        elif not stack and paren:
            return False
        else:
            top = stack.pop()
            if top + paren not in '()[]{}<>':
                return False
    return True if not stack else False
