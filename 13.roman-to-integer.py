#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ROM2INT = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000,
        }

        prev_num = 0
        sums = 0
        for char in s:
            cur = ROM2INT[char]
            sums += cur
            if prev_num < cur:
                sums -= 2 * prev_num
            prev_num = cur
        return sums

        
# @lc code=end

