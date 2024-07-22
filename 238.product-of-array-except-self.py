#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import numpy as np
        # prefix product
        left_array = [1] * len(nums)
        right_array = [1] * len(nums)

        for i in range(1, len(nums), 1):
            left_array[i] = left_array[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_array[i] = right_array[i+1] * nums[i+1]
        
        return list(np.array(left_array) * np.array(right_array))
        
# @lc code=end

