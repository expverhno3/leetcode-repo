#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # --- must check: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems/?source=vscode 
        T_ik0 = 0 # no profit at start
        T_ik1 = float('-inf') # not gonna happen to have a stock at the beginning
        for price in prices:
            T_ik0_old = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price - fee) # rest or sell
            T_ik1 = max(T_ik1, T_ik0_old - price) # rest or buy
        return T_ik0

# @lc code=end

