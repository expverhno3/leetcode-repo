#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
from typing import List

"""
[1,17,5,10,13,15,10,5,16,8]
"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # NOTE: greedy
        # 3 cases:
            # 1. up and down -> record the peaks & vallies
            # 2. monotonic up -> take two ends
            # 3. up plateau down (or reversed shape) -> take two vallies and one peak
        if len(nums) < 1:
            return len(nums)
        curDiff = 0
        preDiff = 0
        result = 1
        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1
                preDiff = curDiff
        return result
            
# @lc code=end

