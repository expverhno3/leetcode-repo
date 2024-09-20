#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # bit wise and: x & (x+1) => previous (n-1) bits will stay the same
        # once that digit has been changed, that position must be 0 no matter how many times it changed
        # --- impl by: https://leetcode.com/problems/bitwise-and-of-numbers-range/solutions/4759881/beats-100-users-c-java-python-javascript-explained/?source=vscode
        # cnt = 0
        # while left != right:
        #     left >>= 1
        #     right >>= 1
        #     cnt += 1
        # return left << cnt
        
        # a little bit optimized for cases that left reached 0 already -> no need to do more (all prefixes run out and all different) -> just return 0
        counter = 0
        while left != right:
            if left == 0:
                return left
            left >>= 1
            right >>= 1
            counter += 1
        return left << counter


# @lc code=end

