#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        
        # definition of dp[i]: for integer i, number of unique BST
        # state transfer: root node start from 1 to i, and number of different structures on left sub-tree is: dp[j-1], and right sub-tree is: dp[i-j]

        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        
        return dp[n]
        


# @lc code=end

