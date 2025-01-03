#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        # (0,3,1) <, (0,0,1) -> 0
        # (0,3,1) >, (2,3,2) == -> 2
        # (0,3,1) <, (0,0,1) -> 1
        # (0,3,1) >, (2,3,2) >, (3,3,2) -> 4

        # left closed, right open
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] == target:
        #         return mid
        #     else:
        #         right = mid - 1
        # if nums[left] >= target:
        #     return left
        # elif nums[left] < target:
        #     return left + 1
        
        # left, right are both closed
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return left
            
        
# @lc code=end

