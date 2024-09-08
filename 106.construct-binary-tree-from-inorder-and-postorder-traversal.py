#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Construct Binary Tree from Inorder and Postorder Traversal
        """
        # if inorder is empty, return None
        if not inorder:
            return None
        # if inorder only has one element, return TreeNode
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            # create a dictionary to map inorder values to their indices
            inorder_val2idx = {val:i for i, val in enumerate(inorder)}
            # define a recursive function to build the tree
            def recur(left_idx_inorder: int, right_idx_inorder: int) -> Optional[TreeNode]:
                # if left > right or postorder is empty, return None
                if left_idx_inorder > right_idx_inorder or not postorder:
                    return None
                else:
                    # pop the last element from postorder as the root value
                    root_val = postorder.pop()
                    # create a TreeNode with the root value
                    root = TreeNode(root_val)
                    # create a dictionary to map inorder values to their indices
                    root_inorder_idx = inorder_val2idx[root_val]
                    # recursively build the right subtree
                    root.right = recur(root_inorder_idx+1, right_idx_inorder)
                    # recursively build the left subtree
                    root.left = recur(left_idx_inorder, root_inorder_idx-1)
                    return root
            # call the recursive function with the full range of inorder
            return recur(0, len(inorder)-1)
        
        
# @lc code=end

