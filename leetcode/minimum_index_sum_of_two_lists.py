class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_idxs = {}

        for i, r in enumerate(list1):
            if r in list2:
                min_idxs[r] = i + list2.index(r)

        return [k for k, v in min_idxs.items() if v == min(min_idxs.values())]