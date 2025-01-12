#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # --- recursion (depth first)
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            # it's post-order
            return max(dfs(root.left), dfs(root.right)) + 1

        return dfs(root)


        # --- My Implementation: level order ---
        # if not root:
        #     return 0
        # queue = deque([root])
        # counter = 0
        
        # while queue:

        #     level_length = len(queue)

        #     for i in range(level_length):
        #         node = queue.popleft()
                
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     counter += 1
        # return counter

        
        
# @lc code=end

