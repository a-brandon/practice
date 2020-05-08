def rgb_to_hex(col):
    colors = col.replace('rgb(', '').replace(')', '').split(',')
    nums = list(map(int, colors))
    conversion = ''.join('00' if n == 0 else hex(n)[2:] for n in nums)
    return '#' + conversion
