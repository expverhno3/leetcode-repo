#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        
        # both right and left are closed interval
        while left <= right:
            mid = (left + right) // 2
            mid2 = mid * mid
            if mid2 == num:
                return True
            elif mid2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

