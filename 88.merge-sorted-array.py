#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        i = m - 1 # largest in nums1
        j = n - 1 # largest in nums2
        k = m + n - 1 # largest in total nums
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# @lc code=end

