#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = (left + right) // 2
        res = guess(mid)

        while res != 0:
            if res == -1:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
            res = guess(mid)
        return mid
        
# @lc code=end

