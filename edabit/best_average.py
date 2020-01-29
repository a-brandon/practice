def get_best_student(grades):
    student_averages = {}
    for k, v in grades.items():
        student_averages[k] = sum(v) / len(v)
    return max(student_averages, key=student_averages.get)
