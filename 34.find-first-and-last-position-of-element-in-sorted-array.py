#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums)-1
        is_found = False
        while left <= right:
            mid = (left + right) // 2
            print(f"{left}, {right}, {mid}")
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                is_found = True
                break
        if not is_found:
            return [-1, -1]

        left_res = right_res = mid
        while left_res >= 0 and nums[left_res] == target:
            left_res -= 1
        left_res += 1
        while right_res < len(nums) and nums[right_res] == target:
            right_res += 1
        right_res -= 1
        return [left_res, right_res]


# @lc code=end
