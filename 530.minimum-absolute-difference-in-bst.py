#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')
        def dfs(r:TreeNode):
            nonlocal prev, min_diff
            if not r:
                return
            dfs(r.left)
            if prev:
                min_diff = min(r.val - prev.val, min_diff)
            prev = r
            dfs(r.right)
            return
        dfs(root)
        return min_diff
# @lc code=end

