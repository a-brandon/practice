class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        max_num = num

        for i, n in enumerate(s):
            if n == '6':
                s[i] = '9'
                changed_num = int(''.join(s))
                if changed_num > max_num:
                    max_num = changed_num
                    s[i] = '6'
                else:
                    s[i] = '6'

        return max_num