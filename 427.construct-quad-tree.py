#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from typing import List
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    """
    Construct Quad Tree
    """
    def construct(self, grid: List[List[int]]) -> Node:
        """
        main function to construct quad tree
        """
        return self._helper(grid, 0, 0, len(grid))

    def _helper(self, grid, row_start, col_start, width):
        """
        helper function to construct quad tree

        Args:
            grid (List[List[int]]): input grid
            row_start (int): start row of current node
            col_start (int): start column of current node
            width (int): width of current node

        Returns:
            Node: constructed node
        """
        if self._allSame(grid, row_start, col_start, width):
            # all cells are the same
            return Node(grid[row_start][col_start] == 1, True)

        node = Node(True, False)
        # construct 4 children
        node.topLeft = self._helper(grid, row_start, col_start, width // 2)
        node.topRight = self._helper(grid, row_start, col_start + width // 2, width // 2)
        node.bottomLeft = self._helper(grid, row_start + width // 2, col_start, width // 2)
        node.bottomRight = self._helper(grid, row_start + width // 2, col_start + width // 2, width // 2)

        return node

    def _allSame(self, grid, row_start, col_start, width):
        """
        check if all cells in a rectangle are the same

        Args:
            grid (List[List[int]]): input grid
            row_start (int): start row of current node
            col_start (int): start column of current node
            width (int): width of current node

        Returns:
            bool: True if all cells are the same, False otherwise
        """
        for row in range(row_start, row_start + width):
            for col in range(col_start, col_start + width):
                if grid[row][col] != grid[row_start][col_start]:
                    return False
        return True
    # --- my impl -> max recursion depth exceeds :(
    # def construct(self, grid: List[List[int]]) -> 'Node':
    #     dummy = Node(True, False)
    #     n = len(grid)
    #     n_half = n // 2 # start idx of right/bottom half
    #     if n == 2:
    #         topleft = grid[0][0]
    #         topright = grid[0][1]
    #         bottomleft = grid[1][0]
    #         bottomright = grid[1][1]
    #         if topleft == topright == bottomleft == bottomright:
    #             dummy.isLeaf = True
    #             dummy.val = topleft
    #         else:
    #             dummy.topLeft = Node(topleft, True)
    #             dummy.topRight = Node(topright, True)
    #             dummy.bottomLeft = Node(bottomleft, True)
    #             dummy.bottomRight = Node(bottomright, True)
    #     else:
    #         dummy.topLeft= self.construct(grid[:n_half][:n_half])
    #         dummy.topRight = self.construct(grid[:n_half][n_half:])
    #         dummy.bottomLeft = self.construct(grid[n_half:][:n_half])
    #         dummy.bottomRight = self.construct(grid[n_half:][n_half:])
    #     return dummy        


# @lc code=end

