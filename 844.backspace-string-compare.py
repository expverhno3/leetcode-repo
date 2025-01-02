#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(s:str):
            slow = 0
            s = list(s)
            for fast in range(len(s)):
                if s[fast] == "#":
                    slow = slow - 1 if slow > 0 else 0
                else:
                    s[slow] = s[fast]
                    slow += 1
            return ''.join(s[:slow])
        return remove(s) == remove(t)
        
# @lc code=end

