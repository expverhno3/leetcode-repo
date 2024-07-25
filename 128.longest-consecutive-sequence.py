#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        length = 0
        nums_set = set(nums)
        for num in nums:
            if (num - 1) not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                res = max(res, length)
        return res

                

        
# @lc code=end

