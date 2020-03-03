def dice_game(lst):
    score = 0
    for x, y in lst:
        if x == y:
            return 0
        else:
            score += x + y
    return score
