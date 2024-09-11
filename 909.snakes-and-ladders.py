#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from typing import List, Set
from collections import deque

"""
[[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]
"""
class Solution:
    def snakesAndLadders(self, board):
        """
        Snakes and Ladders

        :param board: 2D array, representing the board
        :return: the minimum number of moves to reach the last cell

        The algorithm is as follows:

        1. Initialize a queue with the start node (1), and its distance from the start node (0)
        2. While the queue is not empty, pop the node from the queue
        3. For each possible move (up to 6 steps forward), check if the destination is reachable (not blocked by snakes or ladders)
        4. If reachable, mark the destination as reachable and add it to the queue
        5. When the queue is empty, return the distance of the last cell

        """
        n = len(board)

        def i2coordinate(i:int):
            """
            convert the index to (row, column) coordinates

            :param i: the index of the cell
            :return: (row, column) coordinates

            """
            i -= 1
            row = n - 1 - i // n
            direction = ((row % 2) == 1) if n % 2 == 0 else ((row % 2) == 0) # true if goes from left to right
            col = i % n if direction else n-1 - i % n
            return (row, col)
        
        dist = [-1] * (n * n + 1)
        dist[1] = 0
        queue = deque([1])
        while queue:
            curr = queue.popleft()
            for next in range(curr + 1, min(curr + 6, n * n) + 1):
                row, column = i2coordinate(next)
                destination = board[row][column] if board[row][column] != -1 else next
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    queue.append(destination)
        return dist[n * n]
        
# @lc code=end

