#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        #note: solution from others: https://leetcode.com/problems/rotate-string/solutions/3005884/python3-good-enough/
        for i in range(len(s)):
            if goal[0] == s[i]: # only compares first char
                if s[i:] + s[:i] == goal: # only compare entire string when there's a chance!
                    return True
        return False

        #note: my solution
        # if len(s) != len(goal):
        #     return False

        # padding_str = s + s + s       

        # for i in range(len(s)):
        #     if padding_str[i:len(s)+i] == goal:
        #         return True
        # return False
        
# @lc code=end

