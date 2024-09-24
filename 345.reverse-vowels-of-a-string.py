#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        left, right = 0, len(s) - 1
        
        s = list(s)

        while left < right:
            
            while left < len(s) and s[left] not in VOWELS:
                left += 1
            if left > right or left >= len(s): break
            while s[right] not in VOWELS:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
        
# @lc code=end

