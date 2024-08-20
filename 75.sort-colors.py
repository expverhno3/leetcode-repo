#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #NOTE: low -> end of "0" section (all elements before low are 0s);
        #NOTE: mid -> iterate through entire array
        #NOTE: high -> beginning of "2" (all elements after high are 2s)
        low = mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # add a 0 to "low" region, expand boundary
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # as wanted, do nothing but move on
                mid += 1
            else:
                # add a 2 to "high" region, expand boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                #! don't increment mid here: swapped to mid can be 0, require further process
        
                

        
# @lc code=end

