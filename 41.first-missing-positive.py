#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # copilot is just brilliant...
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] # swap num with nums[num-1] -> nums[num-1] should == num

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
        
# @lc code=end

