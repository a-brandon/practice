def find_fulcrum(lst):
    fulcrums = []
    for i, x in enumerate(lst):
        left, right = sum(lst[:i]), sum(lst[i + 1:])
        if left == right:
            fulcrums.append(x)
    return fulcrums[0] if fulcrums else -1
