#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # --- impl: 1D (hard)
        # reduction of space origins from observation that dp[i][j] in the 2D DP array depends only on dp[i-1][j] and dp[i][j-1] -> use 1 row to do this!
        m, n, l = len(s1), len(s2), len(s3)

        if m + n != l:
            return False
        
        if m < n:
            # len(s2) must > len(s1)
            return self.isInterleave(s2, s1, s3)

        # init
        dp = [False] * (n+1)
        dp[0] = True

        for j in range(1, n+1):
            # test if all s2 can make up s3
            dp[j] = dp[j-1] and (s3[j-1] == s2[j-1])
        
        for i in range(1, m+1):
            # come from previous s1 char
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                # check if it's come from s1 or s2
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]


        # --- impl: 2D matrix
        # """
        # meaning of dp[i][j]: whether s1[:i] and s2[:j] can be interleaved to form s3[:i+j]
        # new coming element at (i,j): s1[i-1] or s2[j-1] and s3[i+j-1]
        # """
        # if len(s1) + len(s2) != len(s3):
        #     return False

        # dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # for i in range(len(s1) + 1):
        #     for j in range(len(s2) + 1):
        #         if i == 0 and j == 0:
        #             dp[i][j] = True
        #         elif i == 0:
        #             # come from previous column
        #             dp[i][j] = dp[i][j-1] and s3[i+j-1] == s2[j-1]
        #         elif j == 0:
        #             # come from previous row
        #             dp[i][j] = dp[i-1][j] and s3[i+j-1] == s1[i-1]
        #         else: # may come from both direction
        #             dp[i][j] = (dp[i][j-1] and s3[i+j-1] == s2[j-1]) or (dp[i-1][j] and s3[i+j-1] == s1[i-1])
                    

        # return dp[-1][-1]
# @lc code=end

