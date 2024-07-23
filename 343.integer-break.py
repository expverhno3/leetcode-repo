#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        import math
        if n <= 3: return n - 1
        a, b = n // 3, n % 3 # a -> how many 3s; b -> remainder
        if b == 0: return int(math.pow(3, a)) # no remainder, perfect
        if b == 1: return int(math.pow(3, a - 1) * 4) # break 3 + 1 into 2 + 2
        return int(math.pow(3, a) * 2) # remainder == 2

# @lc code=end

