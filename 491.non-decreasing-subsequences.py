#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
from typing import List

# class Solution:
#     def findSubsequences(self, nums):
#         result = []
#         path = []
#         self.backtracking(nums, 0, path, result)
#         return result
    
#     def backtracking(self, nums, startIndex, path, result):
#         if len(path) > 1:
#             result.append(path[:])  # 注意要使用切片将当前路径的副本加入结果集
#             # 注意这里不要加return，要取树上的节点
        
#         uset = set()  # 使用集合对本层元素进行去重
#         for i in range(startIndex, len(nums)):
#             if (path and nums[i] < path[-1]) or nums[i] in uset:
#                 continue
            
#             uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
#             path.append(nums[i])
#             self.backtracking(nums, i + 1, path, result)
#             path.pop()

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        def backtracking(startIdx, path):
            if len(path) >= 2:
                nonlocal res
                res.append(path[:])
            level_set = set()
            for i in range(startIdx, n):
                if (path and nums[i] < path[-1]) or nums[i] in level_set:
                    continue
                level_set.add(nums[i])
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()
        backtracking(0, [])
        return res
            
        
# @lc code=end

