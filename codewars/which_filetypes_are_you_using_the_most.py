def solve(files):
    file_lookup = {}
    for f in files:
        ext = f[f.rindex('.'):]
        if ext not in file_lookup:
            file_lookup[ext] = 1
        else:
            file_lookup[ext] += 1

    return sorted(k for k, v in file_lookup.items() if v == max(file_lookup.values()))