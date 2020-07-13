class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(heights[i] != sorted(heights)[i] for i, _ in enumerate(heights))