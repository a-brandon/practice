class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []

        res = []

        for x in nums1:
            loc = nums2.index(x)

            if nums2[-1] == nums2[loc]:
                res.append(-1)
            else:
                rem = nums2[loc + 1:]

                i = 0
                while i < len(rem):
                    if rem[i] > x:
                        res.append(rem[i])
                        break
                    i += 1
                else:
                    res.append(-1)

        return res
