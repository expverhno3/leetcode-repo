#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
from typing import List
from heapq import heappush, heappop


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i = 0
        j = len(costs) - 1
        heap1 = []
        heap2 = []

        res = 0
        while k > 0:
            while len(heap1) < candidates and i <= j:
                heappush(heap1, costs[i])
                i += 1
            while len(heap2) < candidates and i <= j:
                heappush(heap2, costs[j])
                j -= 1
            t1 = heap1[0] if heap1 else float('inf')
            t2 = heap2[0] if heap2 else float('inf')
            if t1 <= t2:
                res += t1
                heappop(heap1)
            else:
                res += t2
                heappop(heap2)
            k -= 1
        return res
            
        
# @lc code=end

