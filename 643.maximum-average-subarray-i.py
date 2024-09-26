#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # use a sliding window to keep track of the sum of the last k numbers
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]

        # keep track of the max sum of any subarray of length k
        max_sum = window_sum

        # slide the window to the right and update the window sum
        # by subtracting the leftmost number and adding the new rightmost number
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, window_sum)

        # return the average of the max sum
        return max_sum / k
                


# @lc code=end

