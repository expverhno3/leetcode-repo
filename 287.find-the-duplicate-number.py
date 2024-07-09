#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # --- version from others:
        slow = nums[0] # use values as index, step once
        fast = nums[slow] # step twice
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        #note: reset
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        



        # --- my version: sort then find if there's duplicate next to each other
        # sorted_nums = sorted(nums)
        # for i, num in enumerate(sorted_nums):
        #     if (i+1) < len(nums) and num == sorted_nums[i+1]:
        #         return num
            
# @lc code=end

