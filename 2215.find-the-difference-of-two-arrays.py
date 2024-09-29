#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uniq_nums1 = set(nums1)
        uniq_nums2 = set(nums2)

        res1 = []
        res2 = []

        for num in uniq_nums1:
            if num not in uniq_nums2:
                res1.append(num)
        for num in uniq_nums2:
            if num not in uniq_nums1:
                res2.append(num)
        return [res1, res2]


        
# @lc code=end

