class Solution:
    def countBits(self, num: int) -> List[int]:
        return [len(bin(i)[2:].replace('0', '')) for i in range(0, num + 1)]