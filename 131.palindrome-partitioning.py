#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List
class Solution:
    def __init__(self):
        from collections import defaultdict
        #NOTE: use memory to save time (string -> all posible palindrome partitioning list)
        self.memory = defaultdict(list)
    
    def _is_valid(self, s:str):
        """check if this string is palindrome"""
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        if not s: # empty string
            return [[]]
        else:
            if s in self.memory: # use memory
                return self.memory[s]
            ans = []
            for i in range(1,len(s)+1):
                if self._is_valid(s[:i]): # prefix is palindrome
                    for suf in self.partition(s[i:]): # partitioning recursively
                        ans.append([s[:i]] + suf) # connect sub string's partitioning answer to prefix
            self.memory[s] = ans # save ans to memory
        return ans
        

        
# @lc code=end

