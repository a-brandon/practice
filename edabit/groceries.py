def get_total_price(groceries: list[dict]) -> float:
    total = 0
    for elem in groceries:
        total += elem['price'] * elem['quantity']
    return float(total)
