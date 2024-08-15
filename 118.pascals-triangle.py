#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        res = [row[:]]
        for _ in range(1, numRows):
            row_1 = [0] + row
            row_2 = row + [0]
            row = [i + j for i,j in zip(row_1, row_2)]
            res.append(row[:])
        return res
# @lc code=end

