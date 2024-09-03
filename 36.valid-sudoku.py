#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Checks if a given Sudoku board is valid.

        Args:
            board: A 9x9 grid of characters representing the Sudoku board.

        Returns:
            True if the board is valid, False otherwise.
        """
        # --- impl: use separate functions
        # 1. check if each row valid
        # 2. check if each col valid
        # 3. check if each block (3 x 3 board) valid

        def isUnitValid(row_or_col: List[str]):
            # take actual unit out
            units = [s for s in row_or_col if s != "."]
            # check if all units are unique
            return len(set(units)) == len(units)

        def isRowValid(board):
            for row in board:
                if not isUnitValid(row):
                    return False
            return True
        
        def isColumnValid(board):
            for col in zip(*board):
                if not isUnitValid(col):
                    return False
            return True
        
        def isBlockValid(board):
            for i in range(3):
                for j in range(3):
                    if not isUnitValid([board[i*3+k][j*3+l] for k in range(3) for l in range(3)]):
                        return False
            return True

        return isRowValid(board) and isBlockValid(board) and isColumnValid(board)



        # --- impl: encode position in a special way + hashmap
        # seen = set()

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             b = f"({board[i][j]})"
        #             if not (b + str(i)) in seen and not str(j) + b in seen and not str(i // 3) + b + str(j // 3) in seen:
        #                 seen.add(b + str(i))
        #                 seen.add(str(j) + b)
        #                 seen.add(str(i // 3) + b + str(j // 3))
        #             else:
        #                 return False

        # return True
# @lc code=end

