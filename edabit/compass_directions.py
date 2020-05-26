def final_direction(initial, turns):
    directions = ['N', 'E', 'S', 'W'] * len(turns)
    compass = {'L': -1, 'R': 1}
    start = directions.index(initial)
    for t in turns:
        start += compass[t]
    return directions[start]
