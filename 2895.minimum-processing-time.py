#
# @lc app=leetcode id=2895 lang=python3
#
# [2895] Minimum Processing Time
#

# @lc code=start
from typing import List
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()

        res = 0
        right = len(tasks) - 1

        for i in range(len(processorTime)):
            cur = processorTime[i] + tasks[right]
            res = max(cur, res)
            right -= 4
            if right < 0:
                break
        
        return res
            
# @lc code=end

