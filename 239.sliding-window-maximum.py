#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # note: naive trial, just keep the value of maximum, rather than keep the index of all potential maximum value
        # left = 0
        # right = left + k - 1
        # max_value = max(nums[left:right+1])
        # res = [max_value]
        # left += 1
        # right += 1
        # while right < len(nums):
        #     if nums[left-1] == max_value:
        #         if nums[right] > max_value:
        #             max_value = nums[right]
        #         else:
        #             max_value = max(nums[left:right+1])
        #     elif nums[right] > max_value:
        #         max_value = nums[right]
        #     res.append(max_value)
        #     left += 1
        #     right += 1

        # note: solution from others
        res = []
        left, right = 0, 0
        nums_length = len(nums)
        q = deque()  # queue saved all

        while right < nums_length:
            while (
                q and nums[q[-1]] < nums[right]
            ):  # if the new incoming value is greater than the last value in deque
                q.pop()

            q.append(
                right
            )  # always append right side index in queue, on the left side of queue, the index correspond to larger value, while right side has smaller value

            if q[0] < left:  # max value index out of range
                q.popleft()

            if (
                right + 1 >= k
            ):  # window is formed, need to adjust left pointer & append max value to res
                res.append(nums[q[0]])
                left += 1

            right += 1

        return res


# @lc code=end
