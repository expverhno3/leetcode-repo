#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
from heapq import heappop, heappush, heappushpop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        while nums:
            if len(heap) < k:
                heappush(heap, nums.pop())
            else:
                heappushpop(heap, nums.pop())
                    
        return heappop(heap)

        



        
# @lc code=end

