#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

# test case: [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        def dfs(root:Optional[TreeNode]):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left + right) # NOTE: just save max diameter during find depth!
            return 1 + max(left, right)

        dfs(root)
        return self.diameter

        #--- impl at first (depth, and find max diameter)
        # if not root:
        #     return 0
        # def dfs(root:Optional[TreeNode]):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left), dfs(root.right)) + 1
        # #NOTE: num_of_edges = depth of tree - 1
        # # return dfs(root.left) - 1 + dfs(root.right) - 1 + 2
        # # return dfs(root.left) + dfs(root.right)
        # def dfs2(root:TreeNode):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left)+dfs(root.right), dfs2(root.left), dfs2(root.right))
        # return dfs2(root)
        


# @lc code=end

