class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            x, y = stones[-2], stones[-1]

            if x == y:
                stones.remove(x)
                stones.remove(y)
            else:
                stones[stones.index(y)] = y - x
                stones.remove(x)

        return stones[0] if stones else 0