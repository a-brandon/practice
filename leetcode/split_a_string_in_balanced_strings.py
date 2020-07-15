class Solution:
    def balancedStringSplit(self, s: str) -> int:
        splits = {'L': 0, 'R': 0}
        counter = 0

        for ch in s:
            splits[ch] += 1
            if splits['R'] == splits['L']:
                counter += 1
                splits['R'] = 0
                splits['L'] = 0

        return counter