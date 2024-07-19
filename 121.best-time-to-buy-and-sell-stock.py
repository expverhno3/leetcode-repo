#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, (price - cost))
        return profit
        
# @lc code=end

