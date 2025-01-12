#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node:TreeNode, isLeft:bool=False):
            if not node:
                return 0
            if not node.left and not node.right:
                if isLeft:
                    return node.val
                else:
                    return 0
            else:
                left_val = dfs(node.left, isLeft=True)
                right_val = dfs(node.right)
                return left_val + right_val
        return dfs(root)
        
# @lc code=end

