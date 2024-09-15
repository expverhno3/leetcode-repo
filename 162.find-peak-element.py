#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        #NOTE: 4 cases:
        # 1. up -> down -> up: return leftmost or rightmost
        # 2. up: return rightmost
        # 3. down: return leftmost
        # 4. down -> up -> down: return middle

        left, right = 0, len(nums)-1

        while left < right:
            
            mid = (left + right) // 2

            # case 4
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            # case 2 and case 1
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            # case 3
            else:
                right = mid - 1

        return left
# @lc code=end

