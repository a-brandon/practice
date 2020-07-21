class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lookup = {n: arr1.count(n) for n in arr2}
        l = []
        excl_elems = sorted(x for x in arr1 if x not in arr2)

        for k, v in lookup.items():
            l.extend([k] * v)

        return l + excl_elems