#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        #note: padding
        len_diff = len(num1) - len(num2)
        if len_diff > 0:
            num2 = "0" * len_diff + num2
        else:
            num1 = "0" * (-len_diff) + num1

        res = ''
        of = 0
        for i in range(len(num1)-1, -1, -1):
            sumi = int(num1[i]) + int(num2[i]) + of
            of = int(sumi > 9)
            res = str(sumi)[-1] + res
        if of:
            res = str(of) + res
        return res


        
# @lc code=end

