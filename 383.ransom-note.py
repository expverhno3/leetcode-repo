#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        ransomNote_freq_table = Counter(ransomNote)
        magazine_freq_table = Counter(magazine)

        unique_chars = set(ransomNote)

        for c in unique_chars:
            if not ransomNote_freq_table[c] <= magazine_freq_table[c]:
                return False
        return True
        

        
# @lc code=end

