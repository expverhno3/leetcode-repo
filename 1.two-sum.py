#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2idx = {}
        for i, num in enumerate(nums):
            if num not in val2idx:
                val2idx[num] = [i]
            else:
                val2idx[num].append(i)
        
        for num in nums:
            num_complement = target - num
            if num_complement in val2idx:
                if num_complement != num:
                    return [val2idx[num][0], val2idx[num_complement][0]]
                if num_complement == num and len(val2idx[num]) > 1:
                    return [val2idx[num][0], val2idx[num][1]]
                    


        # left, right = (0, target) if target > 0 else (target, 0)
        # while True:
        #     if left in val2idx and right in val2idx:
        #         if left != right:
        #             return [val2idx[left][0], val2idx[right][0]]
        #         else:
        #             if len(val2idx[left]) > 1:
        #                 return [val2idx[left][0], val2idx[left][1]]
        #     left += 1
        #     right -= 1
            

# @lc code=end

