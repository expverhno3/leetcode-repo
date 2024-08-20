#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # min : (small -> large)
        # max : (large -> small)
        # middle: (small -> large -> [pivot] -> large -> small)
        # its next: (small -> large -> [minimumly larger than pivot] -> small -> large (reverse this region))
        
        n = len(nums)

        # find pivot (smaller than its immediate right)
        pivot = n-2
        while nums[pivot] >= nums[pivot+1] and pivot >= 0:
            pivot -= 1
        
        if pivot == -1:
            nums.reverse()
            return
        
        # find "successor", i.e. a number at pivot right && minimumly larger than pivot
        successor = -1
        for i in range(n-1,pivot,-1):
            if nums[i] > nums[pivot]:
                # iterate in ascending order
                successor = i
                break
        
        # swap successor and pivot
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # reverse array after pivot
        nums[pivot+1:] = reversed(nums[pivot+1:])

        
# @lc code=end

