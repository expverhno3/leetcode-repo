#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        CLOSE = ")"
        OPEN = "("
        # init dp table: dp[i] represent longest valid parentheses length that ends at index i
        dp = [0] * len(s)
        res = 0

        for i in range(1,len(s)):
            char = s[i]
            if char == OPEN:
                continue
            if char == CLOSE:
                if s[i-1] == OPEN:
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                # NOTE: i -> current idx; dp[i-1] -> longest valid parentheses end at i-1; i-dp[i-1] -> say i==3, jump from end of (()) to first "(", i.e. 1; i-dp[i-1]-1 -> first char
                #NOTE: this condition used to add a pair that WRAP pairs that represented by dp[i-1]
                elif s[i-1] == CLOSE and i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == OPEN:
                    dp[i] = dp[i-1] + 2

                    # if there's continual parentheses just before the beginning of current combination
                    if i - dp[i-1] >= 2:
                        dp[i] += dp[i - dp[i-1] - 2]
                res = max(res, dp[i])
        return res
                
        
        
# @lc code=end

