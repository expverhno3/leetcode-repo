#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        current_sum = 0
        def recur(root:TreeNode):
            nonlocal current_sum
            
            current_sum += root.val
            if not root.left and not root.right:
                # leaf node
                if current_sum == targetSum:
                    return True

            # not leaf
            else:
                if root.left:
                    left = recur(root.left)
                    if left:
                        return True
                if root.right:
                    right = recur(root.right)
                    if right:
                        return True
            
            current_sum -= root.val
            return False
        return recur(root)
                
                
            
                


        return recur(root)
            
        
# @lc code=end

