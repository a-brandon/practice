def find_double(n):
    double = str(n)[0]
    for n in str(n[1:]):
        if n != double[-1]:
            double += '.'
        double += n
    double = [d for d in double.split('.') if len(d) == 2]
    return double


def triple_double(num1, num2):
    num1, num2 = str(num1), str(num2)
    triple = num1[0]
    for n in num1[1:]:
        if n != triple[-1]:
            triple += '.'
        triple += n
    triple = [trip for trip in triple.split('.') if len(trip) == 3]
    dub = find_double(num2)
    for digit in dub:
        if digit[:] == triple[0][0:2]:
            return 1
    return 0
