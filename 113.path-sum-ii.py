#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        prev_nodes = []
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            else:
                prev_nodes.append(root.val)
                if not root.left and not root.right: # root is leaf node
                    if sum(prev_nodes) == targetSum:
                        ans.append(prev_nodes[:]) # ! make a copy

                else:
                    dfs(root.left)
                    if prev_nodes and root.left:
                        prev_nodes.pop()
                    dfs(root.right)
                    if prev_nodes and root.right:
                        prev_nodes.pop()

        dfs(root)
        return ans
# @lc code=end

