def group_seats(lst, n):
    seats = [*sum(lst, [])]
    zeros = [i for i, x in enumerate(seats) if x == 0]
    avail_seats = 0
    for i, _ in enumerate(zeros[:-n + 1]):
        placements, counter = zeros[i:i + n], 0
        if all(placements[j] + 1 == placements[j + 1] or placements[j + 1] - 1 ==
               placements[j] for j, _ in enumerate(placements[:-1])):
            avail_seats += 1
    return avail_seats
