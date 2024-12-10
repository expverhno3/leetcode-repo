#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - k*2, 0)
        
# @lc code=end

