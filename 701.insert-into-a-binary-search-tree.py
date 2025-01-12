#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif root.val < val and not root.right:
            root.right = TreeNode(val)
            return root
        elif root.val >= val and not root.left:
            root.left = TreeNode(val)
            return root
        elif val > root.val:
            self.insertIntoBST(root.right, val)
        else:
            self.insertIntoBST(root.left, val)
        return root
            
        
# @lc code=end

