#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, upperbound, lowerbound):
            if not root:
                return True
            if lowerbound < root.val < upperbound:
                return helper(root.left,root.val,lowerbound) and helper(root.right, upperbound, root.val)
        return helper(root, float('inf'), -float('inf'))
                
            
        
# @lc code=end

