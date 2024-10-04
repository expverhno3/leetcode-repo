#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root:TreeNode, prev_max):
            if not root:
                return
            if root.val >= prev_max:
                nonlocal res
                res += 1
                prev_max = root.val
            dfs(root.left, prev_max)
            dfs(root.right, prev_max)
        dfs(root, -float('inf'))
        return res 
        
# @lc code=end

