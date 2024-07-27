#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # from https://leetcode.com/problems/subarray-sum-equals-k/solutions/1759711/python-simple-python-solution-using-prefixsum-and-dictionary/comments/1474372
        # NOTE: use prefix sum!

        from collections import defaultdict

        #NOTE: sum_counter's key: prefix sum's value; value: how many times it appear at prefix sum now
        current_sum, res, sum_counter = 0, 0, defaultdict(int)

        for num in nums:
            current_sum += num  # calculate the overall sum
            res += sum_counter.get(current_sum - k, 0)
            sum_counter[current_sum] += 1
        
        return res


# @lc code=end
