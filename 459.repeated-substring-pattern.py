#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        print(s)
        prefix_table = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j>0 and s[j] != s[i]:
                j = prefix_table[j-1]
            if s[i] == s[j]:
                j += 1
            prefix_table[i] = j
        if prefix_table[-1] != 0 and len(s) % (len(s) - prefix_table[-1]) == 0:
            return True
        return False
        
# @lc code=end

