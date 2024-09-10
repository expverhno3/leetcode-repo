#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            num_nodes_cur_level = len(queue)
            cur_sum = 0
            for _ in range(num_nodes_cur_level):
                node = queue.popleft()
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_sum / num_nodes_cur_level)
        return res
            

        
# @lc code=end

