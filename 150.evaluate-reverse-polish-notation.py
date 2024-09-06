#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div(a, b):
            if (a >= 0 and b > 0) or (a < 0 and b < 0):
                return a // b
            else:
                return - (abs(a) // abs(b))
            
        def add(a, b):
            return a + b
        def sub(a, b):
            return a - b
        def mul(a, b):
            return a * b
        OPRAND = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
        }
        stack = []
        for token in tokens:
            if token in OPRAND:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(OPRAND[token](op1,op2))
            else:
                stack.append(int(token))
        return stack.pop()
# @lc code=end

