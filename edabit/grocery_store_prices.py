def get_prices(lst):
    return [float(food.split()[-1][2:-1]) for food in lst]