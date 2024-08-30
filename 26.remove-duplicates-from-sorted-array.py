#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        anchor = 0
        explorer = 0
        counter = 0
        uniques = []

        while explorer < n:
            if nums[explorer] not in uniques:
                uniques.append(nums[explorer])
                nums[explorer], nums[anchor] = nums[anchor], nums[explorer]
                counter += 1
                anchor += 1
            explorer += 1
        return counter



        
# @lc code=end

