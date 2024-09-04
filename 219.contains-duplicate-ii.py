#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Given an array of integers, find if the array contains any duplicates within k places.

        Args:
            nums (List[int]): The input array.
            k (int): The number of places to check for duplicates.

        Returns:
            bool: True if any duplicates are found within k places, False otherwise.
        """
        seen = {}  # Maps a number to its most recent index.
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False

        
# @lc code=end

