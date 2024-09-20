#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        if digits[i] != 9:
            digits[i] += 1
            return digits
        while digits[i] == 9:
            digits[i] = 0
            if i - 1 < 0:
                digits.insert(0, 1)
                return digits
            i -= 1
        digits[i] += 1
        return digits
# @lc code=end

