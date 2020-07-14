class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds, evens = [], []

        for n in A:
            if n % 2:
                odds.append(n)
            else:
                evens.append(n)

        sorted_arr = [odds.pop() if i % 2 else evens.pop() for i in range(len(A))]

        return sorted_arr