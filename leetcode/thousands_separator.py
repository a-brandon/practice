class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = str(n)
        grouping = [num[::-1][i: i + 3] for i in range(0, len(num), 3)]
        rev_nums = [g[::-1] for g in grouping][::-1]
        return ('{}.' * len(rev_nums)).format(*rev_nums)[:-1]