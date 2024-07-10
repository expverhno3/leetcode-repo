#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """recursion"""
        if not root or root == p or root == q: 
            #NOTE: if node to locate LCA are at root, then root is LCA
            return root

        #NOTE: both p and q not in root:
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            #NOTE: if both branch found LCA -> only because themselves == root.right or root.left
            return root
        else:
            #NOTE: only one branch found: one node is the LCA of the other
            return l or r
        
        
        

        
# @lc code=end

