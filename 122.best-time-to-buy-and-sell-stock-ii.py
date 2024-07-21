#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            current_profit = prices[i] - prices[i-1] # profit if buy stock yesterday
            if current_profit > 0:
                profit += current_profit
        return profit
        
# @lc code=end

