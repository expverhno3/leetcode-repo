#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node:TreeNode, path:List[TreeNode]):
            path.append(node.val)
            if not node.left and not node.right:
                nonlocal result
                result.append("->".join([str(v) for v in path]))
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()
        if not root:
            return []
        dfs(root, [])
        return result
        
# @lc code=end

