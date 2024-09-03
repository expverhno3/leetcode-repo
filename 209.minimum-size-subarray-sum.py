#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque
        res = 0
        window = deque([])
        current_sum = 0

        for i in range(len(nums)):
            num = nums[i]
            window.append(num)
            current_sum += num
            if current_sum >= target:
                diff = current_sum - target
                while diff >= window[0]:
                    tmp = window.popleft()
                    current_sum -= tmp
                    diff -= tmp
                res = min(res, len(window)) if res > 0 else len(window)
        return res

                

        
# @lc code=end

