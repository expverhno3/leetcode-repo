#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        range_set = set(range(len(nums)+1))
        nums_set = set(nums)
        return next(iter(range_set.difference(nums_set)))
        
        
# @lc code=end

