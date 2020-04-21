class Solution:   
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if s[0] in ')}]':
            return False

        stack = []
        for paren in s:
            if paren in '({[':
                stack.append(paren)
            elif not stack and paren in ')}]':
                return False
            else:
                top = stack.pop()
                if top + paren not in ['()', '{}', '[]']:
                    return False

        return True if not stack else False
