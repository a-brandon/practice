class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        f, r = sorted(arr), sorted(arr, reverse=True)
        diff = f[1] - f[0]

        for i, x in enumerate(f[:-1]):
            if f[i + 1] - diff != f[i]:
                return False

        for j, y in enumerate(r[:-1]):
            if f[j + 1] - diff != f[j]:
                return False

        return True