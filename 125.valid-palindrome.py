#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.strip()
        if not s or len(s) == 1:
            return True
        left, right = 0, len(s) - 1
        while left < len(s) and not s[left].isalnum():
            left += 1
        while right >= 0 and not s[right].isalnum():
            right -= 1
        while left <= right:
            if s[left] != s[right]:
                print(f"left@{left}, right@{right}, {s[left]} != {s[right]}")
                return False
            left += 1
            while left < len(s) and not s[left].isalnum():
                left += 1
            right -= 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
        return True
        
        
# @lc code=end

