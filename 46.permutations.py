#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def backtracking(path: List[int]):
            if len(path) == n:
                # nonlocal res
                res.append(path[:])
                return
            # nonlocal used
            for i in range(n):
                if used[i]:
                    continue
                else:
                    used[i] = True
                    path.append(nums[i])
                    backtracking(path)
                    path.pop()
                    used[i] = False
        backtracking([])
        return res

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     def dfs(fixed_position: int):
    #         if fixed_position == len(nums) - 1: # reach last position, record this permutation
    #             res.append(list(nums))
    #             return
    #         for i in range(fixed_position, len(nums)):
    #             nums[i], nums[fixed_position] = nums[fixed_position], nums[i] # swap
    #             dfs(fixed_position + 1)
    #             nums[i], nums[fixed_position] = nums[fixed_position], nums[i] # return back
    #     dfs(0)
    #     return res


# @lc code=end
