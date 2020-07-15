class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_count = max(candies)
        return [True if c + extraCandies >= max_count else False for c in candies]