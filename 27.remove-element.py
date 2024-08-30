#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        anchor = 0
        explorer = 0
        n = len(nums)
        counter = 0
    
        while explorer < n:
            if nums[explorer] != val:
                nums[explorer], nums[anchor] = nums[anchor], nums[explorer]
                anchor += 1
                counter += 1
            explorer += 1
        print(nums)
        return counter
        
                

        
# @lc code=end

