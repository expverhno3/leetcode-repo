#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        max_val = 0

        def get_height(which_short, left, right):
            if which_short:
                return height[right]
            return height[left]


        while left < right:
            which_short = 1 if height[left] > height[right] else 0 # 0 -> left is shorter
            temp = (right - left) * get_height(which_short, left, right)
            max_val = temp if temp > max_val else max_val
            if which_short:
                right -= 1
            else:
                left += 1
        return max_val
# @lc code=end
