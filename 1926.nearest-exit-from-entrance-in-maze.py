#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # --- impl from: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/solutions/1329445/an-analysis-on-time-limit-exceeded-tle/?source=vscode (correct mistake of duplicate elements in queue)
        m = len(maze)
        n = len(maze[0])
        
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = 'x'
        count = 0

        while q:
            for _ in range(len(q)):
                cur_pos = q.popleft()
                cur_row, cur_col = cur_pos[0], cur_pos[1]
                if (cur_row == 0 or cur_col == 0 or cur_row == m - 1 or cur_col == n - 1) and count != 0:
                    return count
                if cur_col - 1 >= 0 and maze[cur_row][cur_col-1] == ".":
                    q.append([cur_row, cur_col-1])
                    maze[cur_row][cur_col-1] = 'x'
                if cur_col + 1 <= n-1 and maze[cur_row][cur_col+1] == ".":
                    q.append([cur_row, cur_col+1])
                    maze[cur_row][cur_col+1] = 'x'
                if cur_row + 1 <= m - 1 and maze[cur_row+1][cur_col] == ".":
                    q.append([cur_row+1, cur_col])
                    maze[cur_row+1][cur_col] = 'x'
                if cur_row - 1 >= 0 and maze[cur_row-1][cur_col] == ".":
                    q.append([cur_row-1, cur_col])
                    maze[cur_row-1][cur_col] = 'x'
            count += 1
        return -1
        # --- my impl: memory exceed :(
        # m = len(maze)
        # n = len(maze[0])
        
        # q = deque([entrance])
        # count = 0

        # while q:
        #     for _ in range(len(q)):
        #         cur_pos = q.popleft()
        #         cur_row, cur_col = cur_pos[0], cur_pos[1]
        #         maze[cur_row][cur_col] = "x" # mark visited
        #         if (cur_row == 0 or cur_col == 0 or cur_row == m - 1 or cur_col == n - 1) and count != 0:
        #             return count
        #         if cur_col - 1 >= 0 and maze[cur_row][cur_col-1] == ".":
        #             q.append([cur_row, cur_col-1])
        #         if cur_col + 1 <= n-1 and maze[cur_row][cur_col+1] == ".":
        #             q.append([cur_row, cur_col+1])
        #         if cur_row + 1 <= m - 1 and maze[cur_row+1][cur_col] == ".":
        #             q.append([cur_row+1, cur_col])
        #         if cur_row - 1 >= 0 and maze[cur_row-1][cur_col] == ".":
        #             q.append([cur_row-1, cur_col])
        #     count += 1
        # return -1
        


        
# @lc code=end

