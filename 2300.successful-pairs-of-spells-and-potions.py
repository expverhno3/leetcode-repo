#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
from typing import List

"""
[3,1,2]\n[8,5,8]\n16
[14]\n[25,19,30,37,14,30,38,22,38,38,26,33,34,23,40,28,15,29,36,39,39,37,32,38,8,17,39,20,4,39,39,7,30,35,29,23]\n317
"""
import numpy as np
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions) - 1
        def binary_search(target):
            left = 0
            right = n
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        # print(potions)
        for s in spells:
            target = np.ceil(success / s)
            # print(target)
            # print(binary_search(target))
            # print(potions[binary_search(target)-1])
            res.append(n - binary_search(target) + 1)
        return res
        
# @lc code=end

