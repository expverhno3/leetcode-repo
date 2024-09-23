#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1, length2 = len(word1), len(word2)
        is_word1_shorter = length1 < length2
        smaller_length = length1 if is_word1_shorter else length2
        i = 0
        res = ""
        while i < smaller_length:
            res += word1[i]
            res += word2[i]
            i += 1
        res += word2[i:] if is_word1_shorter else word1[i:]
        return res
        
# @lc code=end

