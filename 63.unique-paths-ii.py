#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # --- better impl from: https://leetcode.com/problems/unique-paths-ii/solutions/1180249/easy-solutions-w-explanation-comments-optimization-from-brute-force-approach/?source=vscode
        # dp table size: m x (n+1), dp[i][j] stores # of unique paths from (0,0) to (i,j)
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i-1][j-1] == 0 (i.e. no obstacle at (i-1,j-1))
        # dp[i][j] = 0 if obstacleGrid[i-1][j-1] == 1 (i.e. obstacle at (i-1,j-1))
        m, n, dp = len(obstacleGrid), len(obstacleGrid[0]), [[0]*(len(obstacleGrid[0]) + 1)] * 2
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j - 1] if not obstacleGrid[i - 1][j - 1] else 0
        return dp[m & 1][-1]

        # --- init impl: 2D dp, without space optimization
        # # get grid size
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])

        # # init
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        
        # # update
        # for i in range(1, m):
        #     for j in range(1,n):
        #         dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]

        
# @lc code=end

