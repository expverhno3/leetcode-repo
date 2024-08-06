#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #--- impl by: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/37010/share-my-simple-non-recursive-solution-o-1-space-complexity/
        #NOTE: no recursion; from top to down, search rightmost node of left sub-tree, merge it to root, move root down
        if not root:
            return None
        node = root
        
        while node:

            if node.left:
                rightmost_node = node.left
                while rightmost_node.right:
                    rightmost_node = rightmost_node.right
                # found rightmost node of left sub-tree
                rightmost_node.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
                


        #--- my impl
        #NOTE: recursion return the deepest end node of each branch, then connect the end of left branch to the start of right branch & connect start of left branch to root
        # if not root:
        #     return

        # def recur(root: TreeNode):
        #     if (not root.left) and (not root.right):
        #         return root
        #     elif root.right and root.left:
        #         left_end = recur(root.left)
        #         right_end = recur(root.right)
        #         left_end.right = root.right
        #         root.right = root.left
        #         root.left = None
        #         return right_end
        #     elif not root.right and root.left:
        #         left_end = recur(root.left)
        #         root.right = root.left
        #         root.left = None
        #         return left_end
        #     elif not root.left and root.right:
        #         right_end = recur(root.right)
        #         return right_end

        # recur(root)


# @lc code=end
