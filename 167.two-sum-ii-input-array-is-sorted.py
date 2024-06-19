#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import Optional, List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers) - 1
        first = 0
        res = numbers[last] + numbers[first]
        while res != target:
            if res > target:
                last -= 1
            if res < target:
                first += 1
            
            res = numbers[last] + numbers[first]
        first += 1
        last += 1
        return first, last
            
        
# @lc code=end

