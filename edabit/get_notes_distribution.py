from collections import Counter


def get_notes_distribution(students):
    notes = sum((note['notes'] for note in students), [])
    dist = Counter()
    for x in notes:
        if 6 > x >= 1:
            dist[x] += 1
    return dist
