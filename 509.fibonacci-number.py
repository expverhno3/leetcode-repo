#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        #--- K's implementation: dp with space optimization

        # what is fib? fib(n) = fib(n-1) + fib(n-2)
        # or in other word: fib(n+1) = fib(n) + fib(n-1)
        # use `a` for fib(n-1), and `b` for fib(n)

        a, b = 0, 1 # a: fib(0), b: fib(1)
        for _ in range(n):
            a, b = b, a+b # b is always 1 step faster than a. range(n) -> a: fib(n), b: fib(n+1)
        return a



        #--- My implementation: recursion
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)
        
# @lc code=end

