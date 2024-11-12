#
# @lc app=leetcode id=2506 lang=python3
#
# [2506] Count Pairs Of Similar Strings
#

# @lc code=start
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def combine_num(n):
            return n * (n - 1) // 2

        d = {}
        for w in words:
            tmp = list(set(list(w)))
            tmp.sort()
            unique_chars = "".join(tmp)
            d[unique_chars] = d.get(unique_chars, 0) + 1
        res = 0
        for v in list(d.values()):
            if v >= 2:
                res += combine_num(v)

        return res


# @lc code=end
