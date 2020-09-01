def get_best_student(grades):
    grade_lookup = {name: sum(v) / len(v) for name, v in grades.items()}
    return max(grade_lookup, key=grade_lookup.get)