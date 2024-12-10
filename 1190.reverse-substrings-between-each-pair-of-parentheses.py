#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur_string = ''
        for char in s:
            if char == "(":
                stack.append(cur_string)
                cur_string = ''
            elif char == ")":
                cur_string = stack.pop() + ''.join(list(cur_string)[::-1])
            else:
                cur_string += char
        return cur_string
            
                

                
                
# @lc code=end

