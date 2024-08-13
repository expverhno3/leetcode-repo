#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while nums[left] > nums[right]:
            mid = (left+right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # (0,4,2) -> (3,4,3) -> (3,3)
        return nums[left]

        
# @lc code=end

