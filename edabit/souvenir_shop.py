def maximum_items(prices, budget):
    all_items = sorted(int(d[1:]) for d in prices if int(d[1:]) < int(budget[1:]))
    if all_items:
        count, balance = 0, int(budget[1:])
        for cost in all_items:
            balance -= cost
            if balance < 0:
                break
            count += 1
        return count
    return 'Not enough funds!'
