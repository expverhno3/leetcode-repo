#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#

# @lc code=start
from typing import List

"""
[73,55,36,5,55,14,9,7,72,52]\n32\n69
"""

import heapq
from collections import deque

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, dp = 0, 0
        prev = -1
        for i in range(len(nums)):
            if nums[i] < left and i > 0:
                res += dp
            if nums[i] > right:
                dp = 0
                prev = i
            if left <= nums[i] <= right:
                dp = i - prev
                res += dp
        return res
        
# @lc code=end

