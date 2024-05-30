#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}
        for char in s:
            if char not in s_table:
                s_table[char] = 1
            else:
                s_table[char] += 1
        for char in t:
            if char not in t_table:
                t_table[char] = 1
            else:
                t_table[char] += 1
        if s_table == t_table:
            return True
        return False


        
# @lc code=end

