#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_length = len(nums)
        def dfs(state:List[int], start_idx:int):
            nonlocal res
            res.append(state[:])
            if start_idx == nums_length:
                return

            for i in range(start_idx, nums_length):
                state.append(nums[i])
                dfs(state, i+1)
                state.pop()
        dfs([], 0)
        return res
# @lc code=end

