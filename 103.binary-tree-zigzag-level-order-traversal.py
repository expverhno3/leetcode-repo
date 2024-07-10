#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        queue = deque([root])
        direction = False # True: left to right, False: right to left
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)
            if level:
                if not direction:
                    level.reverse()
                res.append(level)
            direction = not direction
        return res
        
# @lc code=end

