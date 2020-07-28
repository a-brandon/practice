def addtoArrayForm(A, K):
    return list(map(int, str(int(''.join(map(str, A))) + K)))