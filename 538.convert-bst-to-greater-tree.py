#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        prev_val = 0
        
        def dfs(node:TreeNode):
            nonlocal prev_val
            if not node:
                return
            dfs(node.right)
            node.val += prev_val
            prev_val = node.val
            dfs(node.left)

        dfs(root)

        return root
        

        
        
# @lc code=end

