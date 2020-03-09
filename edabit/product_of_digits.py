def sum_dig_prod(*args):
    number = [int(i) for i in str(sum(args))]
    prod = 1
    count = 0
    while len(number) > 1:
        for x in number:
            prod *= x
            count += 1
        if count == len(number):
            number = [int(i) for i in str(prod)]
            prod = 1
            count = 0
    return number[0]
