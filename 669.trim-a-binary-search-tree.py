#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
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
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val >= low and root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)


# @lc code=end
