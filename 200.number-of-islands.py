#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ref: https://leetcode.com/problems/number-of-islands/solutions/56340/python-simple-dfs-solution/
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            # if not part of island: return
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] != "1":
                return
            
            # rest of cases i,j is part of islands
            grid[i][j] = "-1" # mark visited
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            return
        
        res = 0 # keep track of # of islands

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    # after dfs, indicate found an island
                    res += 1
        
        return res
                
                
        
        
# @lc code=end

