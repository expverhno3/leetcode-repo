#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [0] # save index of high temp (whose warmer day haven't found yet)
        counter = 0
        for i in range(1, len(temperatures)):
            cur_temp = temperatures[i]
            while stack and cur_temp > temperatures[stack[-1]]:
                cur = stack.pop() # cur is the idx of previous unfound day
                ans[cur] = i - cur
            stack.append(i)
        return ans
                
                

            
        
# @lc code=end

