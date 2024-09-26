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

        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1
        

# @lc code=end

