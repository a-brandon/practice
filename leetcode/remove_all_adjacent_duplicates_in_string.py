class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]

        for c in S[1:]:
            if not stack:
                stack = [c]
            elif c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)