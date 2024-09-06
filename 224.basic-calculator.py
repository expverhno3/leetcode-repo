#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        OPERATOR = "+-"
        BRACKET = "()"
        
        stacks: List[List[int]] = [[]]
        counter_stack = []
        cur_stack = []
        prev_is_num = False
        
        def cal_one_stack(stack:List):
            return sum(stack)
                    
                    
        s = "(" + s + ")" 
                

        for char in s:
            if char == "(":
                stacks.append(cur_stack[:])
                cur_stack.clear()
            elif char == ")":
                op = cal_one_stack(cur_stack)
                cur_stack = stacks.pop()
                if cur_stack and cur_stack[-1] == "-":
                    cur_stack.pop()
                    cur_stack.append(-op)
                else:
                    if cur_stack:
                        cur_stack.pop()
                    cur_stack.append(op)
            elif char in OPERATOR:
                cur_stack.append(char)
                prev_is_num = False
            elif char == " ":
                continue
            else:
                if prev_is_num:
                    cur_stack[-1] = cur_stack[-1] * 10 + int(char) if cur_stack[-1] > 0 else cur_stack[-1] * 10 - int(char)
                else:
                    if cur_stack and cur_stack[-1] == "-":
                        cur_stack.pop()
                        cur_stack.append(-int(char))
                    else:
                        if cur_stack:
                            cur_stack.pop()
                        cur_stack.append(int(char))
                    prev_is_num = True
        return cur_stack[-1]
        

                
            
        
# @lc code=end

