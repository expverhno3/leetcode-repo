#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, current = Counter(nums), 0, 0

        for i in range(max(points.keys())+1):
            prev, current = current, max(current, prev + points[i] * i)
        return current

            
        
# @lc code=end

