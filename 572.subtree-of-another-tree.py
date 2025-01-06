#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
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
    def isMatch(self, rootA: Optional[TreeNode], rootB: Optional[TreeNode]):
        if not rootA and not rootB:
            return True
        elif (rootA and rootB) and rootA.val == rootB.val:
            return self.isMatch(rootA.left, rootB.left) and self.isMatch(
                rootA.right, rootB.right
            )
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and subRoot) or (not subRoot and root):
            return False
        elif self.isMatch(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(
                root.right, subRoot
            )


# @lc code=end
