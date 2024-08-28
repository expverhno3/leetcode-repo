#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # --- finite state machine, my impl

        #NOTE: init
        Q0, Q1 = 0, 0

        # define update rule
        def update(Q0, Q1, x):
            D0 = (~x & Q0) | (~Q1 & Q0) | (~Q1 & x)
            D1 = (Q1 & Q0 & ~x) | (~Q1 & Q0 & x)
            return D0, D1
        
        for num in nums:
            Q0, Q1 = update(Q0, Q1, num)
        
        return ~Q1 & Q0


        # --- answer from leetcode solutions
        # ones, twos = 0, 0
        # for num in nums:
        #     ones = ones ^ num & ~twos
        #     twos = twos ^ num & ~ones
        # return ones
        
# @lc code=end

