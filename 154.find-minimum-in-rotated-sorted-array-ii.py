#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #--- Others: binary search
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        while left < right:
            middle = (left + right) // 2
            print(f"{left}, {middle}, {right}")
            if nums[middle] > nums[right]:
                left = middle + 1
                print("in the right half")
            elif nums[right] > nums[middle]:
                right = middle # middle can be the min
                print("in the left half")
            else: # nums[middle] == nums[right]
                # don't know what's going on, but we are sure if move right back, it can potentially reduce
                right -= 1
                print("move back")
        return nums[left]
        # --- MY IMPL: linear search (80%, 20%)
        # for i, num in enumerate(nums):
        #     if i + 1 < len(nums) and nums[i+1] < num:
        #         return nums[i+1]
        # return nums[0]
        
# @lc code=end

