#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        res = []
        for i in range(len(candies)):
            res.append(candies[i] + extraCandies >= max_num)
        return res

# @lc code=end

