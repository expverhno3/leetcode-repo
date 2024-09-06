#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda l:l[0])
        
        prev_range = points[0]
        counter = 1

        for i, point in enumerate(points, 1):
            start, end = point
            if start <= prev_range[1]:
                # print("within the previous range")
                prev_range[0], prev_range[1] = max(start, prev_range[0]), min(end, prev_range[1])
            else:
                # print("out of prev range")
                counter += 1
                prev_range = point

        return counter

# @lc code=end

