#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 若 current_num > target ，则 target 一定在 current_num 所在 行的上方 ，即 current_num 所在行可被消去。
        # 若 current_num < target ，则 target 一定在 current_num 所在 列的右方 ，即 current_num 所在列可被消去。

        i, j = len(matrix)-1, 0 # start from bottom left
        n, m = len(matrix), len(matrix[0])

        while i >= 0 and j < m:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


# @lc code=end