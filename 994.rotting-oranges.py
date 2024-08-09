#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # --- ref impl, bfs, link: https://leetcode.com/problems/rotting-oranges/solutions/563686/python-clean-well-explained-faster-than-90/

        from collections import deque

        if not grid:
            return -1

        m = len(grid)
        n = len(grid[0])

        current_time = 0  # global time tracking
        fresh_counter = 0  # number of fresh tracking
        rotten_queue = deque([])  # use queue to perform bfs, tracking rotten ones

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_queue.append(
                        (i, j)
                    )  # put coordinate of rotten ones into queue
                elif grid[i][j] == 1:
                    fresh_counter += 1

        while rotten_queue and fresh_counter > 0:

            current_time += 1

            # only consider rotten in previous time step (which will bring new rotten in this time step)
            for _ in range(len(rotten_queue)):
                i, j = rotten_queue.popleft()

                # visit adjacent cells
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy

                    # invalid (empty or out-of-boundary or visited)
                    if (
                        x < 0
                        or x >= m
                        or y < 0
                        or y >= n
                        or grid[x][y] == 0
                        or grid[x][y] == 2
                    ):
                        continue

                    if grid[x][y] == 1:
                        fresh_counter -= 1
                        grid[x][y] = 2
                        rotten_queue.append((x, y))

        return current_time if fresh_counter == 0 else -1

        # --- my impl, not working, shouldn't use dfs
        # if not grid:
        #     return -1

        # m = len(grid)
        # n = len(grid[0])

        # def dfs_count_rot_days(grid, i, j, cur_day):
        #     if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or grid[i][j] == 3:
        # #         return cur_day
        #     elif grid[i][j] == 1:
        #         grid[i][j] = 3  # mark as rotten
        #         cur_day += 1
        #         up = dfs_count_rot_days(grid, i + 1, j, cur_day)
        #         down = dfs_count_rot_days(grid, i - 1, j, cur_day)
        #         left = dfs_count_rot_days(grid, i, j + 1, cur_day)
        #         right = dfs_count_rot_days(grid, i, j - 1, cur_day)
        #         return max(up, down, left, right)
        #     elif grid[i][j] == 2:
        #         grid[i][j] = 3
        #         up = dfs_count_rot_days(grid, i + 1, j, cur_day)
        #         down = dfs_count_rot_days(grid, i - 1, j, cur_day)
        #         left = dfs_count_rot_days(grid, i, j + 1, cur_day)
        #         right = dfs_count_rot_days(grid, i, j - 1, cur_day)
        #         return max(up, down, left, right)

        # def dfs_if_isolated(grid, i, j):
        #     if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or grid[i][j] == 3:
        #         return 0
        #     elif grid[i][j] == 1:
        #         up = dfs_if_isolated(grid, i + 1, j)
        #         down = dfs_if_isolated(grid, i - 1, j)
        #         left = dfs_if_isolated(grid, i, j + 1)
        #         right = dfs_if_isolated(grid, i, j - 1)
        #         if sum([up, down, left, right]) > 0:
        #             return max(up, down, left, right)  # not isolated
        #         else:
        #             return 0
        #     elif grid[i][j] == 2:
        #         return dfs_count_rot_days(grid, i, j, 0)

        # res = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 2:
        #             res = max(dfs_count_rot_days(grid, i, j, 0), res)
        #         if grid[i][j] == 1:
        #             days = dfs_if_isolated(grid, i, j)
        #             if days == 0:
        #                 return -1  # it's isolated! not possible
        #             else:
        #                 res = max(days, res)
        # return res


# @lc code=end
