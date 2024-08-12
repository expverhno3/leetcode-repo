#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find out k -> how many digits are rotated
        # (1,2,3,4), k=1 -> (3,4,1,2)
        # (0,3,1) -> (0,1,0) -> tail + 1
        left, right = 0, len(nums) - 1
        mid = 0
        k = 0
        while nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        k = right + 1 if right < mid else left
        print(k)
        if k > 0:
            nums =  nums[k:] + nums[:k]
        
        # binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(f"{left}, {right}, {mid}")
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return (mid + k) % len(nums) if k > 0 else mid
        return -1



            
        
        
# @lc code=end

