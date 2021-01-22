class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        i, j = 0, 1

        while i != len(arr):
            sub_arr = arr[i:j]

            if len(sub_arr) % 2 != 0:
                total += sum(sub_arr)

            j += 1

            if len(sub_arr) == len(arr) - i:
                i += 1
                j = i + 1

        return total