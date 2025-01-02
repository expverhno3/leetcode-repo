#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j = 0, n - 1
        for p in range(n-1, -1, -1):
            x, y = nums[i], nums[j]
            if -x > y:
                ans[p] = x * x
                i += 1
            else:
                ans[p] = y * y
                j -= 1
        return ans
        
# @lc code=end

