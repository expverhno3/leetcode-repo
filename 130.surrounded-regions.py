#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
           return

        # Get the dimensions of the board
        rows, cols = len(board), len(board[0])

        # Initialize a list to store the coordinates of the border cells
        border_cells = [(0, k) for k in range(cols)] + \
                      [(rows-1, k) for k in range(cols)] + \
                      [(k, 0) for k in range(rows)] + \
                      [(k, cols-1) for k in range(rows)]

        # Perform a depth-first search from the border cells
        while border_cells:
           row, col = border_cells.pop()
           if (0 <= row < rows) and (0 <= col < cols) and (board[row][col] == 'O'):
               # Mark the cell as visited
               board[row][col] = 'S'

               # Add the neighboring cells to the list
               border_cells.extend([(row, col-1), (row, col+1), (row-1, col), (row+1, col)])

        # Update the board by replacing 'S' with 'O' and 'O' with 'X'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'S':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'

        
# @lc code=end

