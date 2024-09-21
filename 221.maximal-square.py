#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # --- impl by: https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach/?source=vscode
        if not matrix:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    res = max(dp[i+1][j+1], res)
        return res ** 2
        
# @lc code=end

