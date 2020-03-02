def get_prices(arr):
    arr = ''.join(arr)
    dollars = ''
    for c in arr:
        if not c.isalpha():
            dollars += c
    dollars = dollars.split()
    prices = []
    for el in dollars:
        price = el.replace('$', '').replace('(', '').replace(')', '')
        prices.append(price)
    return [float(x) for x in prices]
