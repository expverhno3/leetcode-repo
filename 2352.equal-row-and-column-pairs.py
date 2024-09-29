#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
"""


"""
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        from collections import defaultdict
        freq_table = defaultdict(int)
        
        for row in grid:
            row = tuple(row)
            freq_table[row] += 1


        grid = [*zip(*grid)]
        res = 0
        for col in grid:
            res += freq_table.get(col, 0)
        return res 
            
# @lc code=end

