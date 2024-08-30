#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # --- impl of https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/solutions/27976/3-6-easy-lines-c-java-python-ruby/?source=vscode

        write_pointer = 0
        
        for num in nums:
            # just "rewrite" the array from the beginning, and make sure there's no more than 2 duplicate elements
            if write_pointer < 2 or nums[write_pointer - 2] < num:
                nums[write_pointer] = num
                write_pointer += 1
        
        return write_pointer
                
            
            
        
# @lc code=end

