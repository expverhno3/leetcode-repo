#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xffffffff # mask
        a, b = a & x, b & x # take last 32 bits
        # 循环，当进位为 0 时跳出
        while b != 0:
            # a, b = 非进位和, 进位
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x) # return back to Python's weired negative representation

# @lc code=end

