class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {}

        for i in range(lo, hi + 1):
            count, x = 0, i

            while x > 1:
                if not x % 2:
                    x //= 2
                    count += 1
                else:
                    x = (3 * x) + 1
                    count += 1

            powers[i] = count

        return sorted(powers, key=powers.get)[k - 1]