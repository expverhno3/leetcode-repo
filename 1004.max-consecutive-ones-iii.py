#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # --- impl from: https://leetcode.com/problems/max-consecutive-ones-iii/solutions/247564/java-c-python-sliding-window/?source=vscode

        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1
        

        

# @lc code=end

