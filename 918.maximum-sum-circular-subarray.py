#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, maxSum, minSum = 0, -float('inf'), float('inf')
        # `prev_sum_max` is the max sum of subarray ending at current index
        # `prev_sum_min` is the min sum of subarray ending at current index
        prev_sum_max, prev_sum_min = 0, 0
        for num in nums:
            # `total` is the sum of all elements in the array
            # used to calculate the sum of the circular subarray
            total += num
            # update `prev_sum_max` to be the max of current number and the sum of current number and the previous max sum
            prev_sum_max = max(num, prev_sum_max + num)
            # update `maxSum` to be the max of current `maxSum` and the new `prev_sum_max`
            maxSum = max(maxSum, prev_sum_max)
            # update `prev_sum_min` to be the min of current number and the sum of current number and the previous min sum
            prev_sum_min = min(num, prev_sum_min + num)
            # update `minSum` to be the min of current `minSum` and the new `prev_sum_min`
            minSum = min(minSum, prev_sum_min)
        # `maxSum` is the max sum of subarray in the array
        # `total - minSum` is the sum of the circular subarray
        # return the max of two
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum

        #NOTE: way to find max subarray without circular
        # maxSum = -float('inf')
        # prev_sum = maxSum
        # for num in nums:
        #     if num > prev_sum + num:
        #         prev_sum = num
        #     else:
        #         prev_sum += num
        #     maxSum = max(prev_sum, maxSum)
        # return maxSum
# @lc code=end

