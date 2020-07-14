class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums, min_nums = [], {min(el) for el in matrix}

        for col in zip(*matrix):
            m = max(col)
            if m in min_nums:
                lucky_nums.append(m)

        return lucky_nums