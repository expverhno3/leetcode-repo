#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s)+1, len(p)+1
        dp = [[False]*n for _ in range(m)]

        # init dp table
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"
        
        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] == "*":
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and s[i-1] == p[j-2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and p[j-2] == ".":
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if dp[i-1][j-1]:
                        if s[i-1] == p[j-1] or p[j-1] == ".":
                            dp[i][j] = True
                    else:
                        dp[i][j] = False
        return dp[-1][-1]
                        
        


        

# @lc code=end

