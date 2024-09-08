#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recur(p, q):
            if not p and not q:
                return True
            elif (not p and q ) or (p and not q):
                return False
            if p.val == q.val:
                left = recur(p.left, q.left)
                if left:
                    right = recur(p.right, q.right)
                    if right:
                        return True
            return False
        
        return recur(p,q)
        
# @lc code=end

