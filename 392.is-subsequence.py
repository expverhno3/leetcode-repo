#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        # t_pointer = 0
        len_s = len(s)
        res = ''
        if not s:
            return True
        else:
            for char in t:
                if s_pointer < len_s and char == s[s_pointer]:
                    s_pointer += 1
                    res += char
            return res == s
                

            
        # if not s:
        #     return True
        # s_pointer = -1
        # current_pointer = 0
        # target_len = len(t)
        # while current_pointer < target_len:
        #     if t[current_pointer] == s[s_pointer+1] and s_pointer < len(s) - 2:
        #         s_pointer += 1
        #     current_pointer += 1
        # return s_pointer == len(s) - 1 and s_pointer != -1

        
# @lc code=end

