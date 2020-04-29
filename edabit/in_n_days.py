def after_n_days(days, n):
    d = 3 if n == 1 else n
    weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
             'Friday', 'Saturday', 'Sunday'] * d
    return [weeks[weeks.index(x) + n] for x in days]
