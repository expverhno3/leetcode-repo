#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            half = len(x_str) // 2 if len(x_str) % 2 == 0 else len(x_str) // 2 + 1
            
            left = 0
            while left < half:
                if x_str[left] != x_str[-1-left]:
                    return False
                left += 1
            return True
                
        
# @lc code=end

