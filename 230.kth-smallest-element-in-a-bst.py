#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    
    # --- 1. in-order traverse
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     vals = []
    #     self.inOrder(root, vals, k)
    #     return vals[k-1]
        
    
    # def inOrder(self, root: TreeNode, vals: List[int], k):
        
    #     if root is None:
    #         return
        
    #     self.inOrder(root.left, vals, k)
    #     if len(vals) >= k:
    #         return
    #     vals.append(root.val)
    #     self.inOrder(root.right, vals, k)

    # --- 2. in-order traverse, use counter to save memory & run faster
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.count = 0
        self.inOrder(root)
        return self.res
        
    
    def inOrder(self, root: TreeNode):
        
        if root is None:
            return
        
        self.inOrder(root.left)
        self.count += 1
        if self.count == self.k:
            self.res = root.val
        self.inOrder(root.right)


# @lc code=end

