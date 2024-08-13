#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Finds the median of two sorted arrays.

        Args:
            nums1: The first sorted array.
            nums2: The second sorted array.

        Returns:
            The median of the combined arrays.
        """

        #NOTE: Ensure nums1 is always the shorter array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # m < n
        m, n = len(nums1), len(nums2)
        total = m + n

        # Calculate the index of the left median element
        # (total=5, lefthalf=3) (total=6, lefthalf=3)
        left_half_len = (total + 1) // 2

        # Binary search on the shorter array to find the partition
        low, high = 0, m
        while low <= high:
            partition_x = (low + high) // 2 # guess the start of right half partition at first array
            partition_y = left_half_len - partition_x # guess the start of right half partition at second array

            # Get the elements to compare from both arrays
            max_left_x = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float("inf") if partition_x == m else nums1[partition_x]
            max_left_y = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float("inf") if partition_y == n else nums2[partition_y]

            # Check if the partition is correct
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Even number of elements
                if total % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                # Odd number of elements
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                # Too many elements in left half of nums1
                high = partition_x - 1
            else:
                # Too few elements in left half of nums1
                low = partition_x + 1

        return 0  # Should not reach here
        
# @lc code=end

