#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        res = max_so_far
        for i in range(1,len(nums)):
            num = nums[i]
            max_so_far, min_so_far = max(num, max_so_far * num, min_so_far * num), min(num, max_so_far * num, min_so_far * num)
            res = max(res, max_so_far)

        return res

        
# @lc code=end

