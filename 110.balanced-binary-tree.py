#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""a binary tree in which the height of the left and the right subtree of any node differ by not more than 1"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root: TreeNode):
            # empty node
            if not root:
                return 0
            # access max depth of left node
            left = dfs(root.left)
            if left == -1:
                return -1
            
            # access max depth of right node
            right = dfs(root.right)
            if right == -1:
                return -1
            
            # return max depth of current node (max left or right depth + 1), and pruning if unbalanced
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        res = dfs(root)
        if res == -1:
            return False
        return True
            

# @lc code=end

