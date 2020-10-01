def average_string(s):
    if not s:
        return 'n/a'

    num_lookup = {'zero': 0, 'one': 1, 'two': 2,
                  'three': 3, 'four': 4, 'five': 5,
                  'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9}
    num_lookup = {**num_lookup, **{v: k for k, v in num_lookup.items()}}

    nums = s.split()
    total = 0
    for n in s.split():
        if n not in num_lookup:
            return 'n/a'
        total += num_lookup[n]

    return num_lookup[total // len(nums)]