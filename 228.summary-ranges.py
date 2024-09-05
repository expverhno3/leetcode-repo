#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Given a sorted integer array, return the summary of the ranges in the form of a string.
        Example: [0, 1, 2, 4, 5, 7] -> ["0->2", "4->5", "7"]
        """
        result = []
        if not nums:
            return result
        start_of_range = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # Start a new range
                if start_of_range == nums[i - 1]:
                    result.append(str(start_of_range))
                else:
                    result.append(str(start_of_range) + "->" + str(nums[i - 1]))
                start_of_range = nums[i]
        # Append the last range
        if start_of_range == nums[-1]:
            result.append(str(start_of_range))
        else:
            result.append(str(start_of_range) + "->" + str(nums[-1]))
        return result
            
        
# @lc code=end

