#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
                return
            dfs(root.left, res)
            dfs(root.right, res)
        set1 = list()
        set2 = list()
        dfs(root1, set1)
        dfs(root2, set2)

        return set1 == set2
# @lc code=end

