def progress_days(runs):
    count = 0
    for i, num in enumerate(runs[:-1]):
        if runs[i + 1] > runs[i]:
            count += 1
    return count
