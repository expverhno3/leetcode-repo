#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        ans = -1
        def dfs(node:TreeNode, depth):
            if not node:
                return
            if not node.left and not node.right:
                nonlocal max_depth, ans
                if depth > max_depth:
                    max_depth = depth
                    ans = node.val
                    return
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            return
        dfs(root, 0)
        return ans
                
        
# @lc code=end

