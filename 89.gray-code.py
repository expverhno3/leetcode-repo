#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, 2 ** n):
            res.append(i ^ (i >> 1))
        return res
            
# @lc code=end

