#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit2letters = {
            '2':('a','b','c'),
            '3':('d','e','f'),
            '4':('g','h','i'),
            '5':('j','k','l'),
            '6':('m','n','o'),
            '7':('p','q','r','s'),
            '8':('t','u','v'),
            '9':('w','x','y','z')
        }
        res = []
        if not digits:
            return res
        def dfs(state:List[str], starting_digits_idx):
            if starting_digits_idx == len(digits) - 1:
                nonlocal res
                for letter in digit2letters[digits[starting_digits_idx]]:
                    state.append(letter)
                    res.append(''.join(state))
                    state.pop()
            else:
                for letter in digit2letters[digits[starting_digits_idx]]:
                    state.append(letter)
                    dfs(state, starting_digits_idx+1)
                    state.pop()
        dfs([],0)
        return res
            
        
# @lc code=end

