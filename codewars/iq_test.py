def iq_test(numbers):
    nums, parity = numbers.split(), {'evens': [], 'odds': []}

    for i in nums:
        parity['evens'].append(i) if int(i) % 2 == 0 else parity['odds'].append(i)

    return nums.index(min((parity['evens'], parity['odds']), key=len)[0]) + 1