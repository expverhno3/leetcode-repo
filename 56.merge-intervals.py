#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            left, right = intervals[i][0], intervals[i][1]
            if left <= res[-1][1]:
                if right > res[-1][1]:
                    res[-1][1] = right
            else:
                res.append(intervals[i])
        return res
            
# @lc code=end

