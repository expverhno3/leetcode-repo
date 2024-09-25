#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    # def maxOperations(self, nums: List[int], k: int) -> int:
        # freq_map = Counter(nums)
        # res = 0
        # for num in nums:
        #     if freq_map[num] > 0:
        #         diff = k - num
        #         freq_map[num] -= 1
        #         if diff in freq_map and freq_map[diff] > 0:
        #             freq_map[diff] -= 1
        #             res += 1
        #         else:
        #             freq_map[num] += 1
        # return res
    def maxOperations(self, nums, k):
        count = 0
        num_counts = {}
        for num in nums:
            res = k - num
            if res in num_counts:
                count += 1
                num_counts[res] -= 1
                if num_counts[res] == 0:
                    del num_counts[res]
            else:
                num_counts[num] = num_counts.get(num, 0) + 1
        return count
                

# @lc code=end

