#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#


# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strNum = str(n)
        flag = len(strNum)
        for i in range(len(strNum) - 1, 0, -1):
            if strNum[i - 1] > strNum[i]:
                flag = i
                strNum = strNum[: i - 1] + str(int(strNum[i - 1]) - 1) + strNum[i:]
        strNum = strNum[:flag] + "9" * (len(strNum) - flag)
        return int(strNum)


# @lc code=end
