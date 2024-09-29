#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        res = 0
        tmp = 0

        for g in gain:
            tmp += g
            res = max(tmp, res)
        return res
            
        
# @lc code=end

