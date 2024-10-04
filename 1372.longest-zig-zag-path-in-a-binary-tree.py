#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 1
        def dfs(root:TreeNode, is_left:bool, counter:int):
            if not root:
                nonlocal res
                res = max(res, counter)
                return
            counter += 1
            if is_left:
                dfs(root.left, not is_left, counter)
                dfs(root.left, is_left, 0)
            else:
                dfs(root.right, not is_left, counter)
                dfs(root.right, is_left, 0)
                
        dfs(root, True, 0)
        dfs(root, False, 0)
        return res - 1
                

            
# @lc code=end

