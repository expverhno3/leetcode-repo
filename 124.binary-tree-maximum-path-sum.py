#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # --- impl ref from: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/
        if not root:
            return 0
        res = -float('inf')
        def recur(root:Optional[TreeNode]):
            """return max gain can get from sub-trees"""
            nonlocal res
            if root is None:
                return 0
            left_gain = max(recur(root.left), 0)
            right_gain = max(recur(root.right), 0)

            current_path_max = root.val + left_gain + right_gain # if only including current node and its childs
            res = max(current_path_max, res)

            return root.val + max(left_gain, right_gain)
        recur(root)
        return res
            
            
                

        return recur(root)
            
            
        
# @lc code=end

