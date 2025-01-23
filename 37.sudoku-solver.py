#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row // 3) * 3 + col // 3].add(num)
        self.backtracking(0, 0, board, row_used, col_used, box_used)

    def backtracking(
        self,
        row: int,
        col: int,
        board: List[List[str]],
        row_used: List[List[int]],
        col_used: List[List[int]],
        box_used: List[List[int]],
    ) -> bool:
        if row == 9:
            return True

        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
        if board[row][col] != ".":
            return self.backtracking(
                next_row, next_col, board, row_used, col_used, box_used
            )

        for num in map(str, range(1, 10)):
            if (
                num not in row_used[row]
                and num not in col_used[col]
                and num not in box_used[(row // 3) * 3 + col // 3]
            ):
                board[row][col] = num
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row // 3) * 3 + col // 3].add(num)
                if self.backtracking(
                    next_row, next_col, board, row_used, col_used, box_used
                ):
                    return True
                board[row][col] = "."
                row_used[row].remove(num)
                col_used[col].remove(num)
                box_used[(row // 3) * 3 + col // 3].remove(num)
        return False


# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         row_used = [set() for _ in range(9)]
#         col_used = [set() for _ in range(9)]
#         box_used = [set() for _ in range(9)]

#         for i in range(9):
#             for j in range(9):
#                 val = board[i][j]
#                 if val == ".":
#                     continue
#                 else:
#                     row_used[i].add(val)
#                     col_used[i].add(val)
#                     box_used[(i // 3) * 3 + j // 3].add(val)
#         self.backtracking(0,0,board, row_used, col_used, box_used)


#     def backtracking(self, row, col, board, row_used, col_used, box_used) -> bool:
#         if row == 9:
#             return True

#         next_row, next_col = (row, col + 1) if col < 8 else (row+1, 0)
#         if board[row][col] != '.':
#             # search next empty element
#             return self.backtracking(next_row, next_col, board, row_used, col_used, box_used)

#         for num in map(str, range(1, 10)):
#             if (
#                 num not in row_used[row] and
#                 num not in col_used[col] and
#                 num not in box_used[(row // 3) * 3 + col // 3]
#             ):
#                 board[row][col] = num
#                 row_used[row].add(num)
#                 col_used[col].add(num)
#                 box_used[(row // 3) * 3 + col // 3].add(num)
#                 if self.backtracking(next_row, next_col, board, row_used, col_used, box_used):
#                     return True
#                 board[row][col] = '.'
#                 row_used[row].remove(num)
#                 col_used[col].remove(num)
#                 box_used[(row // 3) * 3 + col // 3].remove(num)
#         return False

# @lc code=end
