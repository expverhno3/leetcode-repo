#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        is_odd_appear = 0
        for v in Counter(s).values():
            if v % 2 != 0:
                res += v-1
                is_odd_appear = 1
            else:
                res += v
        return res+1 if is_odd_appear else res

        

# @lc code=end

