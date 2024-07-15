#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        min_candidate = min(candidates)
        if min_candidate > target: # no way there's a potential combination
            return []
        
        current_list = [] # current trial of combination
        num_candidates = len(candidates)

        def single_combination(new_target: int, prev_index):
            if new_target < min_candidate:
                return
            else:
                # for i, num in enumerate(candidates):
                for i in range(prev_index, num_candidates):
                    num = candidates[i]
                    if new_target - num > 0:
                        current_list.append(num)
                        single_combination(new_target - num, prev_index=i) # new target, and can only choose choice after and including index i
                    elif new_target - num == 0: # yay! get a possible combination
                        current_list.append(num)
                        res.append(current_list[:])
                    else:
                        continue
                    current_list.pop() # undo choice
        single_combination(target, 0)
        return res
                    

# @lc code=end

