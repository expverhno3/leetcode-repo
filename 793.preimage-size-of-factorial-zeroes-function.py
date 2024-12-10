#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#

# @lc code=start

"""
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120 f(5) = 1
6! = 720 f(6) = 1
7! = 5040 f(7) = 1
"""


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        x_fac = 1
        f_x = 0
        i = 1
        num_digits_i = 1
        result = 0 if k > 0 else 1
        while f_x <= k:
            tmp = x_fac * i
            i += 1
            if i % (10 ** num_digits_i) == 0:
                num_digits_i += 1
            if f_x <= k:
                while tmp % 10 == 0:
                    f_x += 1
                    tmp //= 10
            x_fac = tmp % (10 ** (num_digits_i))
            if f_x == k:
                result += 1
            # print(f"{x_fac, result, f_x, i}")
        return result
                
        
# @lc code=end

