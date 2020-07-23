class Solution:
    def countBits(self, num: int) -> List[int]:
        on_bits = [0]

        for i in range(1, num + 1):
            b = bin(i)[2:].replace('0', '')
            on_bits.append(0 + len(b))

        return on_bits
