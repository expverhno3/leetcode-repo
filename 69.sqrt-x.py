#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # --- initial impl: linear search
        # i = 0
        # while i*i <= x:
        #     i += 1
        # return i-1
        
        # --- binary search
        if x == 1 or x == 0:
            return x
        
        start = 1
        end = x
        
        while start <= end:
            
            mid = int(start + 0.5 * (end - start))
            mid2 = mid * mid

            if mid2 > x:
                end = mid - 1
            elif mid2 == x:
                return mid
            else:
                start = mid + 1
        return start - 1
        
# @lc code=end

