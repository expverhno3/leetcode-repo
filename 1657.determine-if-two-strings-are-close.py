#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        c1 = Counter(word1)
        c2 = Counter(word2)

        return set(c1.keys()) == set(c2.keys()) and Counter(c1.values()) == Counter(c2.values())
        
# @lc code=end

