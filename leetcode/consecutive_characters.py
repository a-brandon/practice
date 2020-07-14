class Solution:
    def maxPower(self, s: str) -> int:
        if len(set(s)) == 1:
            return len(s)

        subs = []
        consec_chars = s[0]

        for ch in s[1:]:
            if ch == consec_chars[-1]:
                consec_chars += ch
            else:
                subs.append(consec_chars)
                consec_chars = ch
        subs.append(consec_chars)

        return len(max(subs, key=len))