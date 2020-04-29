def simon_says(lst):
    ops = {'add': '+', 'subtract': '-', 'multiply': '*'}
    curr_num, nums = 0, []
    for command in lst:
        instruction = command.split()
        if instruction[0:2] == ['Simon', 'says']:
            operation, x = instruction[2], instruction[-1]
            curr_num = eval(str(curr_num) + ops[operation] + x)
            nums.append(curr_num)
    return nums[-1] if nums else 0
