#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#


# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        exp = 0
        prev_digits = 0
        prev_prev_digits = 0
        prev_nums = 0
        prev_prev_nums = 0
        while prev_digits < n:
            prev_prev_digits = prev_digits
            prev_prev_nums = prev_nums
            prev_nums = 10 ** exp - 1
            prev_digits = (prev_nums - prev_prev_nums) * exp + prev_prev_digits
            exp += 1
        exp -= 1
        diff = n - prev_prev_digits
        diff_num = (diff-1) // exp
        diff_pos = (diff-1) % exp
        start_num = 10 ** (exp - 1)
        num = start_num + diff_num
        return int(str(num)[diff_pos])

        


# @lc code=end
