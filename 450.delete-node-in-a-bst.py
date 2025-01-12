#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        if root.val == key:
            if not root.right: return root.left
            
            if not root.left: return root.right
            
            if root.left and root.right:
                # temp = root.right
                # while temp.left: temp = temp.left # find node's value closest to root.val, swap with root, and delete it at leaf
                # root.val = temp.val
                # root.right = self.deleteNode(root.right, root.val)
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
# @lc code=end

