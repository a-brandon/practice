class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        split_digits = list(str(n))
        int_list = [int(digit) for digit in split_digits]
        for num in int_list:
            prod *= num
        return prod - sum(int_list)
