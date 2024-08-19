#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp table looks like:
            a c e
          0 0 0 0
        a 0 1 1 1
        b 0 1 1 1
        c 0 1 2 2
        """
        length1, length2 = len(text1), len(text2)
        # make sure text1 is always longer

        dp = [[0] * (length1 + 1) for _ in range(length2 + 1)]

        for i in range(1, length2 + 1):
            for j in range(1, length1 + 1):

                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 # why diagnosis: one row at max increase by 1, avoid repeatedly match results
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[length2][length1]


# @lc code=end
