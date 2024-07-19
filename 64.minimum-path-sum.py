#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        for i in range(1, num_rows):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1, num_cols):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[num_rows-1][num_cols-1]
        
# @lc code=end

