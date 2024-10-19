#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        if n == 0:
            return a
        elif n == 1 or n == 2:
            return c
        
        while n - 3 >= 0:
            a, b, c = b, c, a+b+c
            n -= 1
        return c

# @lc code=end

