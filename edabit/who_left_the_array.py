from collections import Counter


def missing(arr1, arr2):
    if all(type(x) != list for x in arr1 + arr2):
        diff = Counter(arr1) - Counter(arr2)
        return list(diff.keys())[0]
    return [x for x in arr1 if x not in arr2][0]
