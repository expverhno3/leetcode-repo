#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        def dfs(row_state:List[int], col_state:List[int], diag_state:List[int],counter_diag_state:List[int], cur_row):
            if cur_row == n:
                tmp = [["."]*n for _ in range(n)]
                nonlocal res
                for i,j in zip(row_state, col_state):
                   tmp[i][j] = 'Q'
                res.append([''.join(row) for row in tmp][:])
                return

            for y in range(n):
                if cur_row not in row_state and y not in col_state and (cur_row-y) not in diag_state and (cur_row + y) not in counter_diag_state:
                    row_state.append(cur_row)
                    col_state.append(y)
                    diag_state.append(cur_row-y)
                    counter_diag_state.append(cur_row + y)
                    dfs(row_state, col_state, diag_state, counter_diag_state, cur_row+1)
                    row_state.pop()
                    col_state.pop()
                    diag_state.pop()
                    counter_diag_state.pop()
        dfs([],[],[],[],0)
        return res
                        

        
# @lc code=end

