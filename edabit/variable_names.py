def variableValid(var):
    if not var[0].isalpha():
        return False
    else:
        for letter in var:
            if letter == ' ':
                return False
    return True
