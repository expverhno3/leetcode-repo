#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp table: currently min cost to get here
        # dp[i] cost taken to get i
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[-1]
            
        
# @lc code=end

