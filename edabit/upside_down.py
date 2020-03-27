def same_upsidedown(ntxt):
    nums = {'6': '9', '9': '6', '0': '0'}
    opposites = ''
    for n in str(ntxt):
        opposites += nums[n]
    return True if opposites[::-1] == str(ntxt) else False
