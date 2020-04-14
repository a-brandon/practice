def chosen_wine(wines):
    if len(wines) == 1:
        return wines[0]['name']
    if not wines:
        return None
    prices = sorted(wine['price'] for wine in wines)[1]
    for wine in wines:
        if wine['price'] == prices:
            return wine['name']
