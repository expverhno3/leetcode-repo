#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, Dict

# testcase: [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22
# exp: 3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #---impl from: https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/
        # NOTE: main idea: use frequency table to save each old path's sum. if there's an old_path_sum == (cur_path_sum - target), means we get one valid path

        from collections import defaultdict
        res = 0
        cache = defaultdict(int)
        cache[0] = 1

        def dfs(root:TreeNode, targetSum:int, currentSum:int, cache:Dict[int,int]):
            nonlocal res
            if not root:
                return
            currentSum += root.val
            diff = currentSum - targetSum
            # print(f"at {root.val}, diff: {diff}")
            res += cache[diff]
            cache[currentSum] += 1
            dfs(root.left, targetSum, currentSum, cache)
            dfs(root.right, targetSum, currentSum, cache)
            cache[currentSum] -= 1 # cache dict is not local here, and we need to undo it when turn to different branch
        
        dfs(root, targetSum, 0, cache)
        return res
            
            



        # res = 0
        # def recur(root, prev_sum):
        #     nonlocal res
        #     if not root:
        #         return
        #     prev_sum = prev_sum + root.val
        #     if prev_sum == targetSum:
        #         print(f"I'm at {root.val}")
        #         res += 1
        #     recur(root.left, prev_sum)
        #     recur(root.right, prev_sum)
        # recur(root.left, 0)
        # recur(root.right, 0)
        # return res

        
            
        
# @lc code=end

