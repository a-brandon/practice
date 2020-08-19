class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i, n in enumerate(arr):
            sub_arr = arr[i:i + 3]

            if len(sub_arr) == 3 and all(x % 2 for x in sub_arr):
                return True

        return False