#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
            
# @lc code=end

