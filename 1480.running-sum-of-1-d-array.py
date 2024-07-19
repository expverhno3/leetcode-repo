#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[-1] + nums[i])
        return res

                
            
        
# @lc code=end

