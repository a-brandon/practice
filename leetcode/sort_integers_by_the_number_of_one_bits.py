class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bits = {n: bin(n).count('1') for n in arr}
        return sorted(sorted(arr), key=lambda d: bits.get(d))