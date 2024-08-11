#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(state:List[str], currently_open:int, currently_closed:int):
            if currently_open < n:
                state.append('(')
                currently_open += 1
                dfs(state,currently_open, currently_closed)
                state.pop()
                currently_open -= 1
            if currently_closed < currently_open:
                currently_closed += 1
                state.append(')')
                dfs(state, currently_open, currently_closed)
                state.pop()
                currently_closed -= 1
            if currently_open == currently_closed == n:
                nonlocal res
                res.append(''.join(state))
        dfs(['('],1,0)
        return res
        
            
        


# @lc code=end

