class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []

        for i in range(left, right + 1):
            s = str(i)
            if '0' not in s and all(i % int(x) == 0 for x in s):
                nums.append(i)

        return nums   