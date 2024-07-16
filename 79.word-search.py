#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        board_boundary = ((0, len(board)), (0, len(board[0]))) # row boundary, column boundary
        word_length = len(word)

        def dfs(current_row, current_col, wanted_char_index):
            # if out of boundary OR not the char we want: False
            if current_row < 0 or current_col < 0 or current_row >= board_boundary[0][1] or current_col >= board_boundary[1][1] or board[current_row][current_col] != word[wanted_char_index]:
                return False
            
            # code below apply to position that matches char wanted
            if wanted_char_index == word_length-1:
                return True # matched last char

            # matched, but not the last char: search nearby to see if there's a full match 

            board[current_row][current_col] = '' # mark empty, avoid traverse repeatedly
            
            # get result of following chars
            wanted_char_index += 1
            res = dfs(current_row+1, current_col, wanted_char_index) or dfs(current_row, current_col+1, wanted_char_index) or dfs(current_row-1, current_col, wanted_char_index) or dfs(current_row, current_col-1, wanted_char_index)

            # undo trials
            wanted_char_index -= 1
            board[current_row][current_col] = word[wanted_char_index]
            
            return res

        for i in range(board_boundary[0][1]):
            for j in range(board_boundary[1][1]):
                if dfs(i, j, 0):
                    return True
        return False

            


# @lc code=end

