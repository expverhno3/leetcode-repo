#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []
        
        res = []

        def dfs(num_nums_remain, target_sum, prev):
            if target_sum == 0 and num_nums_remain == 0:
                nonlocal res
                res.append(prev[:])
                return
            elif prev and (target_sum < 0 or prev[-1] == 9 or num_nums_remain <= 0 or num_nums_remain <= 0):
                return
            else:
                prev_num = prev[-1] if prev else 0
                for i in range(prev_num+1, 10):
                    prev.append(i)
                    dfs(num_nums_remain-1, target_sum-i, prev)
                    prev.pop()
            return
        dfs(k, n, [])
        return res
# @lc code=end

