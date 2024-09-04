#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
"""
live with number of lives
- <2: dies
- 2<=x<=3: live on next gen
- > 3: dies

dead
- == 3: revive
"""
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def live_or_die(is_live, neighbors):
            sum_lives = sum(neighbors)
            if is_live:
                if sum_lives < 2 or sum_lives > 3:
                    return False
                else:
                    return True
            else:
                if sum_lives == 3:
                    return True
                else:
                    return False

        def get_neighbors(i,j, board=board):
            return [ board[i+k][j+l] for k in range(-1,2) for l in range(-1,2) if 0<= (i+k) < m and 0 <= (j+l) < n and not (k == 0 and l == 0)]
        
        def toggle_state(idx:List[set]):
            for i,j in idx:
                board[i][j] = int(not bool(board[i][j]))
        
        toggle_idx = []
        for i in range(m):
            for j in range(n):
                current_state = board[i][j]
                next_state = live_or_die(current_state, get_neighbors(i,j))
                if current_state != next_state:
                    toggle_idx.append((i,j))
        toggle_state(toggle_idx)
        
        



                
        
# @lc code=end

