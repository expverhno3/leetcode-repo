#
# @lc app=leetcode id=910 lang=python3
#
# [910] Smallest Range II
#

"""
[1,3,6]
[-2,0,3] -> - max
[4,6,9] -> + min
"""

# @lc code=start
from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            # make larger smaller, make smaller larger
            maxi = max(nums[-1] - k, nums[i] + k)
            mini = min(nums[0] + k, nums[i + 1] - k)
            res = min(maxi-mini, res)
        return res


# @lc code=end
