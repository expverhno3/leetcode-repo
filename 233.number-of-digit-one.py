#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#


# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: # if current digit is 0
                res += high * digit
            elif cur == 1: # if current digit is 1
                res += high * digit + low + 1
            else: # other cases
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res


# @lc code=end
