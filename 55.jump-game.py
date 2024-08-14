#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n == 0 :
            return True
        i = 0
        farmost_idx = 0
        while i <= n-1:
            num = nums[i]
            farmost_idx = max(farmost_idx, i+num)
            if farmost_idx >= n:
                return True
            if i == farmost_idx and nums[i] == 0:
                return False
            i += 1
        return False
            


# @lc code=end

