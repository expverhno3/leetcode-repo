#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        i = 1
        VALID_CHARS = '1234567890'
        first_char = s[0]
        if first_char not in VALID_CHARS:
            if first_char == "-":
                is_positive = False
            elif first_char == "+":
                is_positive = True
            else:
                return 0
        else:
            is_positive = True
            i = 0
        res = 0
        while i < len(s) and s[i] in VALID_CHARS:
            res = res * 10 + int(s[i])
            print(res)
            i += 1
        
        if is_positive:
            return min(res, 2**31-1)
        else:
            return max(-res, -(2**31))

# @lc code=end

