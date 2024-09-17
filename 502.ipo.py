#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
from typing import List
from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # --- impl by: https://leetcode.com/problems/ipo/solutions/3219987/day-54-c-priority-queue-easiest-beginner-friendly-sol/?source=vscode
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort(key=lambda x: x[0])
        
        # use a heap to maintain a max heap
        max_heap = []
        current_cap = w
        counter = 0
        pointer = 0
        while counter < k:
            while pointer < len(projects) and projects[pointer][0] <= current_cap:
                heappush(max_heap, -projects[pointer][1])                
                pointer += 1
            if max_heap:
                current_cap += -heappop(max_heap)
                counter += 1
            else:
                # run out of choices! no more projects can be done
                break
        return current_cap

# @lc code=end

