#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1 = dict()

        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 not in d1:
                    d1[n1 + n2] = 1
                else:
                    d1[n1 + n2] += 1
        
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                residual = 0 - (n3 + n4)
                if residual in d1:
                    count += d1[residual]
        return count
                    
        
# @lc code=end

