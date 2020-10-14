def sort_array(source_array):
    if source_array:
        odds, evens = [], []

        for i in source_array:
            if i % 2:
                odds.append(i)
            else:
                evens.append(i)

        odds, evens = sorted(odds)[::-1], evens[::-1]

        return [odds.pop() if i % 2 else evens.pop() for i in source_array]