#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        count1 = [1 for _ in range(len(ratings))]
        count2 = count1[:]

        # only compares current and previous
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                count1[i] = count1[i-1] + 1

        res = count1[-1]
        
        # only compares current and next one, iterate backwards
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                count2[i] = count2[i+1] + 1
            res += max(count2[i], count1[i])
        return res
            



# @lc code=end
