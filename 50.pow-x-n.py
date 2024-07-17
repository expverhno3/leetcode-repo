#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #--- use divide and conquer (fast power analysis)
        if x == 0.0:
            return 0.0

        # init result
        res = 1
        
        # deal with n<0 case
        if n < 0:
            x, n = 1/x, -n # invert x to change n to positive number
        
        # consider n as a binary number, each bit if it's 1 -> accumulate in result; if it's 0 -> just forget it
        while n:
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res




        #--- reach max recursion depth
        # if n == 0:
        #     return 1
        # if n > 0:
        #     return self.myPow(x, n-1) * x
        # if n < 0:
        #     return self.myPow(x, n+1) / x
        
# @lc code=end

