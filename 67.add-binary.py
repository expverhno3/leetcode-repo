#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        b = "0" * (len(a) - len(b)) + b
        
        res = ""
        ab_sum = 0
        for a_char, b_char in zip(a[::-1], b[::-1]):
            a_num = int(a_char)
            b_num = int(b_char)
            ab_sum += a_num + b_num
            res = str(ab_sum % 2) + res
            ab_sum = ab_sum // 2
        if ab_sum != 0:
            res = "1" + res
        return res

# @lc code=end

