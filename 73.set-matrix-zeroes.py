#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # --- better impl from https://leetcode.com/problems/set-matrix-zeroes/solutions/26014/any-shorter-o-1-space-solution/
        m, n, col0 = len(matrix), len(matrix[0]), 1
        
        #NOTE from top to bottom, store state of each row & column (if they should be 0) at the 0th element of that row (or column), since row0 and col0 share the same cell (0,0), this cell used for row0, and use another variable col0 to represent
        for i in range(m):
            # check first column
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # indicate ith row should be all 0
                    matrix[0][j] = 0 # indicate jth column should be all 0
        
        #NOTE: iterate from bottom to top, assign that row or column all 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
            


        # --- my implementation:
        # NOTE: use a list to save all positions of zeros
        # m, n = len(matrix), len(matrix[0])
        # res = []
        # for i in range(m):
        #     for j in range(n):
        #        if matrix[i][j] == 0:
        #            res.append((i,j))
        # for row, column in res:
        #     matrix[row][:] = [0] * n
        #     for i in range(m):
        #         matrix[i][column] = 0
        
# @lc code=end

