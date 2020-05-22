def digital_vowel_ban(n, ban):
    english_nums = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
                    '4': 'four', 'five': '5', '6': 'six',
                    'seven': '7', 'eight': '8', 'nine': '9',
                    'ten': '10'}
    english_nums = {**english_nums, **{v: k for k, v in english_nums.items()}}
    nums = list(map(english_nums.get, str(n)))
    bans = [english_nums[x] for x in nums if ban not in x]
    if bans:
        return n if len(bans) == len(str(n)) else int(''.join(bans))
    return 'Banned Number'
