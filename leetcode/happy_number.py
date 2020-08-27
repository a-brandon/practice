class Solution:
    def isHappy(self, n: int) -> bool:
        tracker = {n: 1}

        while n != 1:
            n = sum(int(x) ** 2 for x in str(n))

            if n in tracker:
                tracker[n] += 1
            else:
                tracker[n] = 1

            if tracker[n] == 2:
                return False

        return True