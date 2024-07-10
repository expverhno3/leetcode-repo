#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #note: how to know which nodes are in the same level
        if not root:
            return []
        res = [[root.val]]
        queue = deque([root])
        
        while queue:
            
            level_length = len(queue)
            level_value = []

            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level_value.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level_value.append(node.right.val)
            if level_value:
                res.append(level_value)
        return res
                


        # --- first version
        # if not root:
        #     return []
        # res = [[root.val]]
        # queue = deque([root])
        # while queue:
        #     tmp = queue.popleft()
        #     res_tmp = []
        #     if tmp.left:
        #         queue.append(tmp.left)
        #         res_tmp.append(tmp.left.val)
        #     if tmp.right:
        #         queue.append(tmp.right)
        #         res_tmp.append(tmp.right.val)
        #     if res_tmp:
        #         res.append(res_tmp)
        # return res

        
        
# @lc code=end

