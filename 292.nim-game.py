#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        # a, b, c = True, True, True
        # if n > 3:
        #     for _ in range(3, n):
        #         a, b, c = (not a or not b or not c), a, b
        # return a
        return n % 4 != 0
        
# @lc code=end

