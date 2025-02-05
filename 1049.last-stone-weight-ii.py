#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        stone_weight_sum = sum(stones)
        target = stone_weight_sum // 2
        dp = [0] * (target + 1)
        for stone in stones:
            for i in range(target, stone-1, -1):
                dp[i] = max(dp[i], dp[i - stone] + stone)
        return stone_weight_sum - 2 * dp[-1]
        
# @lc code=end

