#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """fix left & move middle and right"""
        
        #note: step1, sort the array
        nums.sort()

        res = []
        
        #note: outer loop: move left pointer one step at a time, but considered as fixed when need to find middle and right pointer
        for left in range(len(nums) - 2):
            if nums[left] > 0:
                # you just can't get a 0 from all non-negative numbers
                break
            if left > 0 and nums[left] == nums[left-1]:
                # same number, pass! (not replicate triplets) && avoid compare with last number (all 0 case)
                continue
            middle = left + 1 # middle pointer start from here
            right = len(nums) - 1

            #note: step 2: two sum technique to find
            while middle < right:
                three_sum = nums[left] + nums[middle] + nums[right]
                if three_sum > 0:
                    # too large, move right pointer back
                    right -= 1
                elif three_sum < 0:
                    middle += 1
                else:
                    middle_num = nums[middle]
                    right_num = nums[right]
                    res.append([nums[left], middle_num, right_num])
                    # print(res)
                    #note: step 3, move both pointer until hit different number to check different possibility
                    while middle < right and nums[middle] == middle_num:
                        middle += 1
                    while middle < right and nums[right] == right_num:
                        right -= 1

        return res
# @lc code=end

