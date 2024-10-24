#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        # --- improve with mask
        c_prime = a | b
        diff = c_prime ^ c
        res = 0
        mask = 1

        for _ in range(32):
            if diff & mask > 0:
                res += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1

            mask = mask << 1
        return res

        # --- init impl
        # c_prime = a | b
        # diff = c_prime ^ c
        # res = 0
        # while diff > 0:
        #     is_one = diff & 1
        #     # c_prime is different with c!
        #     if is_one:
        #         flip_one = c_prime & 1
        #         # bit at c is 0, but c_prime is 1
        #         if flip_one:
        #             if a & 1:
        #                 res += 1
        #             if b & 1:
        #                 res += 1
        #         # bit at c is 1, but c_prime is 0
        #         else:
        #             res += 1
        #     diff = diff >> 1
        #     a = a >> 1
        #     b = b >> 1
        #     c_prime = c_prime >> 1
        # return res
                

# @lc code=end

