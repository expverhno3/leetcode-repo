#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count : int = 0
        after_tail_space : bool = False
        while i >= 0:
            if s[i] != " ":
                after_tail_space = True
                count += 1
            else:
                if after_tail_space:
                    return count
            i -= 1
        return count
                
# @lc code=end

