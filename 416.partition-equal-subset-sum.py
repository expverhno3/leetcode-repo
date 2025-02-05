#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_of_nums = sum(nums)

        if sum_of_nums % 2 == 1:
            return False
        
        # --- new solution ---
        # NOTE: convert this problem to a 0/1 knapsack problem
        # each number is a object with weight == value
        # if we can fill a backpack with capacity of sum//2 with value sum//2 -> True
        target = sum_of_nums // 2
        dp = [0] * (target + 1) # weight from 0 to target
        for num in nums:
            for j in range(target, num-1, -1): # reverse order
                dp[j] = max(dp[j], dp[j-num] + num)
        return dp[-1] == target

        # --- old solution ---
        # target = sum_of_nums // 2

        # dp = [False] * (target + 1)
        # dp[0] = True

        # for num in nums:
        #     for j in range(target, num-1, -1):
        #         #! iterate from target to num backwards
        #         # why: we can only use one number for once, and if iterate forward, it's like using this number repeatedly
        #         # for exmaple if num==1 -> all dp table will be True!
        #         if dp[j-num]:
        #             dp[j] = True
        # return dp[target]


        


        
# @lc code=end

