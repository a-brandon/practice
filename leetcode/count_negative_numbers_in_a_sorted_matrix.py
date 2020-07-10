class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(x < 0 for x in sorted(sum(grid, [])))