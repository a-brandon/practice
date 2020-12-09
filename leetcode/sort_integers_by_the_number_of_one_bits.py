class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=lambda i: bin(i)[2:].replace('0', '').count('1'))