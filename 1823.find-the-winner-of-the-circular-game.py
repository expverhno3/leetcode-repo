#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + k % i) % i
        return x + 1

# @lc code=end

