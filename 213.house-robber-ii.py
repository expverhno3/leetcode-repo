#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            if len(nums) == 1:
                return nums[0]
            nums[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                nums[i] = max(nums[i] + nums[i-2], nums[i-1])
            return nums[len(nums)-1] 
        return max( rob1(nums[0:len(nums)-1]), rob1(nums[1:])) if len(nums) > 1 else nums[0]
# @lc code=end

