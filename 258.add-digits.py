#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            tmp = 0
            for c in str(num):
                tmp += int(c)
            num = tmp
        return num
                
            
        
# @lc code=end

