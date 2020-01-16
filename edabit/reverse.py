def reverse(arg):
    if arg:
        return False
    elif str(arg) == 'False':
        return True
    else:
        return 'boolean expected'
