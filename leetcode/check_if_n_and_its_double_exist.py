class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, num in enumerate(arr):
            n = num / 2
            if n in arr and arr.index(n) != i:
                return True
        return False