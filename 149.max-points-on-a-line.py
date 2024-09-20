#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
       # --- impl from https://leetcode.com/problems/max-points-on-a-line/solutions/1983010/python-3-using-slopes-and-hash-tables-clean-python-solution/?source=vscode

        # if len(points) < 3: 
        #    return len(points)

        # def findSlope(point1, point2):
        #    x1, y1 = point1
        #    x2, y2 = point2
        #    if x1 - x2 == 0:
        #        return float('inf')
        #    else:
        #        return (y1 - y2) / (x1 - x2)

        # res = 1
        # for i, p1 in enumerate(points):
        #     slope_counter_map = defaultdict(int)
        #     for p2 in points[i+1:]:
        #         s = findSlope(p1, p2)
        #         slope_counter_map[s] += 1
        #         res = max(slope_counter_map[s], res)
        # return res + 1
        
        from collections import Counter
        
        if len(points) < 3: 
            return len(points)
    
        def findSlope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            if x1 - x2 == 0:
                return float('inf')
            else:
                return (y1 - y2) / (x1 - x2)
    
        res = 1
        for i, p1 in enumerate(points):
            slope_counts = Counter()
            for p2 in points[i+1:]:
                slope = findSlope(p1, p2)
                slope_counts[slope] += 1
            res = max(res, max(slope_counts.values(), default=0) + 1)
        return res
                
# @lc code=end

