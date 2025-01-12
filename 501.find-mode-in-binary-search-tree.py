#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        max_count = 0
        prev = None
        count = 0

        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            
            nonlocal result, max_count, prev, count
            
            if prev is None:
                count = 1
            elif prev == root.val:
                count += 1
            else:
                count = 1
            prev = root.val

            if count == max_count:
                result.append(root.val)
            elif count > max_count:
                max_count = count
                result.clear()
                result.append(root.val)
                
            dfs(root.right)
        
        dfs(root)
        return result
# @lc code=end

