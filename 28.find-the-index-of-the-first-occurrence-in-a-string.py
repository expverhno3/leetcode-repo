#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_idx = 0

        nh = len(haystack)
        nn = len(needle)

        
        while h_idx < nh:

            hchar = haystack[h_idx]
            if hchar == needle[0]:
                if haystack[h_idx:h_idx+nn] == needle:
                    return h_idx
            h_idx += 1
        return -1
        

        
# @lc code=end

