#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # --- solution makes use of BST

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root

        # --- solution using recursion
        # if not root or root == p  or root == q:
        #     return root

        # l = self.lowestCommonAncestor(root.left, p, q)
        # r = self.lowestCommonAncestor(root.right, p, q)

        # if l and r:
        #     return root
        # return l or r


# @lc code=end
