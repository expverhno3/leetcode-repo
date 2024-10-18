#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = math.ceil(sum(piles) / h)
        right = piles[-1]

        def can_finish(k):
            return sum([math.ceil(pile / k) for pile in piles]) <= h
        
        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end

