#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        freq_table = Counter(arr)
        
        values = list(freq_table.values())
        return len(values) == len(set(values))

        
# @lc code=end

