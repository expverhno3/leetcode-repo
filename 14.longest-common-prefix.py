#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = len(strs)
        min_length = min([len(s) for s in strs])
        for i in range(min_length):
            c = strs[0][i]
            for j in range(1,n):
                if strs[j][i] != c:
                    return res
            res += c
        return res
                
        
# @lc code=end

