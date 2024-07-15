#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(fixed_index:int):
            if fixed_index == len(nums) - 1: 
               res.append(list(nums))
               return
            repeat_set = set()
            for i in range(fixed_index, len(nums)):
                if nums[i] in repeat_set: continue
                else:
                    repeat_set.add(nums[i])
                    nums[i], nums[fixed_index] = nums[fixed_index], nums[i]
                    dfs(fixed_index + 1)
                    nums[i], nums[fixed_index] = nums[fixed_index], nums[i]
        dfs(0)
        return res 
        
# @lc code=end

