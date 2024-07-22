#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #--- use property of two's power
        return n > 0 and (n-1) & n == 0


        # --- my implementation
        # if (n % 2 != 0 and n != 1) or (n<=0):
        #     return False
        # if n == 1:
        #     return True
        # while n:
        #     if n % 2 == 1 and n != 1:
        #         return False
        #     n = n // 2
        # return True
            
        
# @lc code=end

