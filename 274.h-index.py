#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        # reversely sorted
        # cited most ith paper -> previously have i papers have more citation -> if citation > i: at least i papers have citations greater than i
        return sum(i < citation for i, citation in enumerate(citations))
        
# @lc code=end

