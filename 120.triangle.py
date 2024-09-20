#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
"""
[[-1],[2,3],[1,-1,-3]]
"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # --- others impl: 1D dp table (https://leetcode.com/problems/triangle/solutions/38730/dp-solution-for-triangle/?source=vscode)
        n = len(triangle)
        dp = triangle[-1][:]

        for k in range(n-2, -1, -1):
            row = triangle[k]
            for i in range(len(row)):
                dp[i] = min(dp[i], dp[i+1]) + triangle[k][i]
        return dp[0]


        # --- my impl: 2D dp table
        # """
        # do dp 2d: same size as triangle
        # dp[i][j] -> ith row, jth index number
        # how update: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        # """
        # n = len(triangle)
        # dp = []
        
        # # init
        # dp.append(triangle[0])
        # for i in range(1, n):
        #     tmp_dp_row = []
        #     for j in range(len(triangle[i])):
        #         if j - 1 < 0:
        #             tmp_dp_row.append(dp[i-1][j] + triangle[i][j])
        #         elif j == i:
        #             tmp_dp_row.append(dp[i-1][j-1]+triangle[i][j])
        #         else:
        #             tmp_dp_row.append(min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j])
        #     dp.append(tmp_dp_row[:])
        # return min(dp[-1])
# @lc code=end

