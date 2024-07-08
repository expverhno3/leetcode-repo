#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2

        while left <= right:
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] == target:
                return middle
            else:
                left = middle + 1
            middle = (left + right) // 2
        return -1
# @lc code=end

