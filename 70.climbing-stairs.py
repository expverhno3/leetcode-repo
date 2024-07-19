#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(1) = 1
        # f(2) = 2
        # f(3) = f(1) + f(2)
        a, b = 1, 2
        for _ in range(n-1):
            a, b = b, a+b
        return a
        
# @lc code=end

