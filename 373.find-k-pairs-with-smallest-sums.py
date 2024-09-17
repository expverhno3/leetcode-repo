#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
from typing import List
from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #NOTE: consider as a matrix: possible next pair should be at either previous_pair's right or below
        heap = []
        length1 = len(nums1)
        length2 = len(nums2)
        def push(i, j):
            if i < length1 and j < length2:
                heappush(heap, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        res = []
        counter = 0
        while heap and counter < k:
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i+1, j)
            counter += 1
        return res
        
# @lc code=end

