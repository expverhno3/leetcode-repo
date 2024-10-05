#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque([root])
        level = 1
        max_sum = -float('inf')
        res = 1

        while q:
            temp = 0
            for _ in range(len(q)):
                node = q.popleft()
                temp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if temp > max_sum:
                res = level
                max_sum = temp
            level += 1
        return res
# @lc code=end

