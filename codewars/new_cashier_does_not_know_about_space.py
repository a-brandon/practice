def get_order(order):
    menu = ['Burger', 'Fries', 'Chicken', 'Pizza',
            'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    res = []

    for f in menu:
        f = f.lower()
        if f in order:
            res.extend([f.capitalize()] * order.count(f))

    return ' '.join(res)