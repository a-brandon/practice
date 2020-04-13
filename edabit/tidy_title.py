def tidy_books(lst):
    res = []
    for book in lst:
        book = ''.join(book).strip().split('-')
        info = [txt.strip() for txt in book]
        res.append(info)
    return res

