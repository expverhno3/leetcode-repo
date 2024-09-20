#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # move answer left 1 bit, and add last bit
            # n & 1: check if last bit is 1
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans

                
        
# @lc code=end

