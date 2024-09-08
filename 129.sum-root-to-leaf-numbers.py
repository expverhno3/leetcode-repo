#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = 0
        
        def dfs(node, cur_num):
            if not node:
                return
            
            cur_num = cur_num * 10 + node.val
            
            if not node.left and not node.right:
                self.res += cur_num
            
            else:
                dfs(node.left, cur_num)
                dfs(node.right, cur_num)
        
        dfs(root, 0)
        
        return self.res
                
# @lc code=end

