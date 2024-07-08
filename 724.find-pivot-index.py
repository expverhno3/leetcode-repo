#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        
        for idx, value in enumerate(nums):
            right_sum -= value
            if left_sum == right_sum:
                return idx
            left_sum += value
        return -1
# @lc code=end

