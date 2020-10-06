def sortFreq(lst):
    return sorted(sorted(lst), key=lst.count, reverse=True)