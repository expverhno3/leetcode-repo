#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self._get_depth(root.left)
        right_depth = self._get_depth(root.right)
        if left_depth == right_depth:
            # looks like:
            #      1
            #    /   \
            #   2     3
            #  / \   /
            # 4   5 6   
            return 2 ** left_depth + self.countNodes(root.right)
        else:
            # looks like:
            #      1
            #    /   \
            #   2     3
            #  / \   / \
            # 4         
            return 2 ** right_depth + self.countNodes(root.left)
        
    def _get_depth(self, root:TreeNode):
        """
        Recursively calculates the depth of a binary tree from a given root node.
        
        Args:
            root (TreeNode): The root node of the binary tree.
        
        Returns:
            int: The depth of the binary tree.
        """
        if not root: return 0
        else:
            return 1 + self._get_depth(root.left)
        
# @lc code=end

