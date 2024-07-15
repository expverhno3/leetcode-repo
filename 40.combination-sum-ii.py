#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #--- way faster
        res = []
        min_candidate = min(candidates)
        if target < min_candidate:
            return []
        candidate_num = len(candidates)
        candidates.sort() # make sure same elements are next to each other
        current_combination = []

        def single_combination(new_target:int, prev_index:int):

            for i in range(prev_index, candidate_num):
                num = candidates[i]
                if i > prev_index and num == candidates[i-1]: #! 限制相等元素在每一轮中只被选择一次
                    continue

                current_combination.append(num) # make choice

                if new_target - num == 0:
                    res.append(current_combination[:])
                elif new_target - num > 0:
                    single_combination(new_target-num, i+1)
                else:
                    current_combination.pop()
                    break

                current_combination.pop()
        
        single_combination(target, 0)
        return res
        
        


        #--- too slow, but worked :(
        # res = []
        # min_candidate = min(candidates)
        # if target < min_candidate:
        #     return []
        # candidate_num = len(candidates)
        
        # current_combination = []

        # def single_combination(new_target:int, prev_index:int):

        #     for i in range(prev_index+1, candidate_num):
        #         num = candidates[i]
        #         current_combination.append(num) # make choice
        #         if new_target - num == 0:
        #             tmp = current_combination[:] # make a copy
        #             tmp.sort() # make sure in res every list is sorted
        #             if tmp not in res: # remove duplicates
        #                 res.append(tmp[:])
        #         elif new_target - num > 0:
        #             single_combination(new_target-num, i)
        #         current_combination.pop()
        
        # single_combination(target, -1)
        # return res
        
# @lc code=end

