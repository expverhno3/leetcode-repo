#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        i = 0
        k = 1
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
            print(k)
        return j - i


# @lc code=end
