def sort_by_answer(lst):
    return sorted(lst, key=lambda e: eval(e.replace('x', '*')))
