def who_passed(students):
    pass_list = []
    for kid in students:
        count = 0
        for score in students[kid]:
            if int(eval(score)) == 1:
                count += 1
            if count == len(students[kid]):
                pass_list.append(kid)
    pass_list.sort()
    return pass_list
