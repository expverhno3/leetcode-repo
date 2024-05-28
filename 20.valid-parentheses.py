#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in r"{[(":
                stack.append(char)
            elif char in r"}])":
                if not stack \
                or (char == "}" and stack[-1] != "{") \
                or (char == "]" and stack[-1] != "[") \
                or (char == ')' and stack[-1] != "("):
                    return False
                else:
                    stack.pop()
        
        return not stack

        
# @lc code=end

