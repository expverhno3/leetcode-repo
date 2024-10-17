#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
from typing import List
from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # --- impl from https://leetcode.com/problems/maximum-subsequence-score/solutions/3082106/java-c-python-priority-queue/?source=vscode
        total = res = 0
        heap = []
        for a, b in sorted(list(zip(nums1, nums2)), key=lambda x: -x[1]):
            heappush(heap, a)
            total += a
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(res, total * b)
        return res
        


        
# @lc code=end

