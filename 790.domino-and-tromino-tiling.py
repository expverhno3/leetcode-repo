#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        # 1->1; 2->2; 3->5 4->(dp[3]+dp[1]) + (dp[2]+dp[2]) + (dp[1]+)
        md = 10**9 + 7
        v = [0] * 1001
        v[1] = 1
        v[2] = 2
        v[3] = 5
        if n <= 3:
            return v[n]
        for i in range(4, n + 1):
            v[i] = 2 * v[i - 1] + v[i - 3]
            v[i] %= md
        return v[n]
# @lc code=end

