class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar",
              "Apr", "May", "Jun",
              "Jul", "Aug", "Sep",
              "Oct", "Nov", "Dec"]
        d = date.split()[::-1]
        m = months.index(d[1]) + 1
        d[1] = str(m) if m >= 10 else f'{0}{m}'
        d[2] = f'{0}{d[2][0]}' if len(d[2]) == 3 else d[2][0:2]

        return '-'.join(d)