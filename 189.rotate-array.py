#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # NOTE: nums = "----->-->"; k =3
        # result = "-->----->";

        # reverse "----->-->" we can get "<--<-----"
        # reverse "<--" we can get "--><-----"
        # reverse "<-----" we can get "-->----->"

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        m = len(nums)
        k = k % m  # reduce operations
        reverse(nums, 0, m - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, m - 1)



        # --- my implementation
        #NOTE: problem: 0 -> 2 -> 0 -> 2 (inf loop :()
        # prev_idx = 0
        # tmp = nums[prev_idx]
        # for i in range(m):
        #     next_idx = (prev_idx + k) % m
        #     nums[next_idx], tmp = tmp, nums[next_idx]
        #     print(f"{prev_idx}, {next_idx}")
        #     prev_idx = next_idx
        
        return None


# @lc code=end
