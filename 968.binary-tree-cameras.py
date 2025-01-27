#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(root: Optional[TreeNode]) -> int:
            # 0: not covered
            # 1: has camera at this node
            # 2: node is covered
            if not root:
                return 2
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l == 2 and r == 2:
                # both left and right are covered
                return 0
            
            # one of left or right is not covered -> this node should have camera
            if l == 0 or r == 0:
                nonlocal count
                count += 1
                return 1
            
            # one of left or right has camera, then current node is covered
            if l == 1 or r == 1:
                return 2

        if dfs(root) == 0:
            count += 1
        return count

# @lc code=end

