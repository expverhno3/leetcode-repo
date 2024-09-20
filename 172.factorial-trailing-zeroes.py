#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # --- sol from: https://leetcode.com/problems/factorial-trailing-zeroes/solutions/52371/my-one-line-solutions-in-3-languages/?source=vscode
        # Because all trailing 0 is from factors 5 * 2.
        # But sometimes one number may have several 5 factors, for example, 25 have two 5 factors, 125 have three 5 factors. In the n! operation, factors 2 is always ample. So we just count how many 5 factors in all number from 1 to n.

        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)


            
# @lc code=end

