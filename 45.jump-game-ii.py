#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # --- impl from https://leetcode.com/problems/jump-game-ii/solutions/18014/concise-o-n-one-loop-java-solution-based-on-greedy
        
        jump_number = 0
        
        if len(nums) == 1:
            return jump_number

        # range of current jump: [current_pointer(i), curEnd] (including both side)
        curEnd = 0
        curFarthest = 0 # farthest idx this jump can get

        for i in range(len(nums)):
            curFarthest = max(curFarthest, i+nums[i])

            if i == curEnd:
                # has to give another jump
                curEnd = curFarthest
                jump_number += 1
                print(f"{jump_number} -> {curEnd}")
                if curEnd >= len(nums) - 1:
                    return jump_number
        return jump_number



        # --- my impl, somehow like dp table :(, slow
        # from collections import defaultdict
        # min_step_table = defaultdict(int)
        # n = len(nums)
        # for i in range(n):
        #     num = nums[i]
        #     max_idx = i + num
        #     start_idx = max(1, i)
        #     cur_min_step = min(i, min_step_table[i]) if i in min_step_table else i
        #     for j in range(start_idx, max_idx+1):
        #         if j in min_step_table:
        #             min_step_table[j] = min(min_step_table[j], cur_min_step+1)
        #         else:
        #             min_step_table[j] = cur_min_step+1
        # return min_step_table[n-1]

                

            

# @lc code=end

