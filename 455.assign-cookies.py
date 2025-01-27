#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        s_idx = 0
        for gi in g:
            while s_idx < len(s) and s[s_idx] < gi:
                s_idx += 1
            if s_idx < len(s):
                res += 1
                s_idx += 1
        return res
                
# @lc code=end

