#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        starts = [i[0] for i in intervals]
        ends = [i[1] for i in intervals]
        starts.sort()
        ends.sort()
        
        s = 0
        e = 0
        res = 0
        while s < len(starts):
            start = starts[s]
            if start <= ends[e]:
                res += 1
            else:
                e += 1
            s += 1
        return res
            
        
# @lc code=end

