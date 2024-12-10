#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums) # use a tail list to record values of longest increasing subsequence
        end_index = 0
        
        for num in nums:

            left, right = 0, end_index # dichotomy pointer
            while left < right:
                middle = (left + right) // 2
                if tails[middle] < num:
                    left = middle + 1
                else:
                    right = middle
            # after dichotomy, left will points to where num should be placed at tails, and `right` should be at 1 step left of `left`
            tails[left] = num
            if right == end_index:
                end_index += 1
        return end_index

        
        
# @lc code=end

