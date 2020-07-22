class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_coords, y_coords = nums[0:n], nums[n:]
        res = []

        for x, y in zip(x_coords, y_coords):
            res.append(x)
            res.append(y)

        return res