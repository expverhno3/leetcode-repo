#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
from typing import List
from heapq import heappush, heappushpop
"""
[1,2,4,2,5,7,2,4,9,0]
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [0,0,2,0,0,3,0,3]
        """
        buy1, buy2, sell1, sell2 = float('inf'), float('inf'), 0, 0

        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            #NOTE: buy2 must be after sell1 (buy2 is should be negative, and buy1 price has passed)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
            print(buy1, buy2, sell1, sell2)

        return sell2


# @lc code=end

