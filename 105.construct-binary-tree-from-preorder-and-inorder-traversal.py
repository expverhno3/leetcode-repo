#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #--- K's Implementation
        def recur(root, left, right):
            # root: index of root value in preorder
            # left: index of left boundary of subtree in inorder
            # right: index of right boundary of subtree in inorder
            if left > right: return                               # 递归终止
            node = TreeNode(preorder[root])                       # 建立根节点
            i = dic[preorder[root]]                               # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i # dic's key: value of node, val: index of node in inorder list, higher efficient
        return recur(0, 0, len(inorder) - 1)


        #--- MY IMPLEMENTATION
        #NOTE: based on pattern below, find the position of starting index of left subtree, right subtree and root, use recursion to build tree (extremely slow)
        """
        preorder: root -> left -> right
        inorder: left -> root -> right
        """
        
        # if not preorder:
        #     return None
        
        # root_val = preorder[0]
        # left_val = inorder[0]
        # root = TreeNode(root_val)

        # if len(preorder) > 1:
        
        #     preorder_root_index = 0
        #     preorder_left_index = 1
        #     inorder_left_index = 0

        #     inorder_root_index = 0        
            
        #     for i, num in enumerate(inorder):
        #         if num == root_val:
        #             inorder_root_index = i
            
        #     inorder_right_index = inorder_root_index + 1

        #     preorder_right_index = (inorder_root_index - inorder_left_index) + preorder_root_index + 1
            
            
        #     left_subtree = self.buildTree(preorder[preorder_left_index:preorder_right_index], inorder[inorder_left_index:inorder_root_index])
        #     right_subtree = self.buildTree(preorder[preorder_right_index:], inorder[inorder_right_index:])
            
        #     root.left = left_subtree
        #     root.right = right_subtree
        # return root
        
        
        
# @lc code=end

