class Solution:
    def numberOfSteps (self, num: int) -> int:
        total = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                total += 1
            elif num % 2 != 0:
                num -= 1
                total += 1
        return total
