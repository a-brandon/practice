def SplitNCases(Str_input, cases):
    length = len(Str_input)
    if cases > length or length % cases:
        return ['Error']

    x = length // cases
    splits = [Str_input[i:i + x] for i in range(0, length, x)]
    return splits