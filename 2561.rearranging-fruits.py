#
# @lc app=leetcode id=2561 lang=python3
#
# [2561] Rearranging Fruits
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # from https://leetcode.com/problems/rearranging-fruits/solutions/3143766/c-java-python3-count-and-match-pairs-o-n-time-complexity-with-quickselect/?source=vscode
        cnt = Counter(basket1)
        for x in basket2:
            cnt[x] -= 1
        last = []
        for k, v in cnt.items():
            # if v is odd, an even distribution is never possible
            if v % 2 != 0:
                return -1
            # the count of transferred k is |v|/2
            last += [k] * abs(v // 2)
        # find the min of two input arrays as the intermediate
        minx = min(basket1 + basket2)
        # Use quickselect instead of sort can get a better complexity
        last.sort()
        # The first half may be the cost
        return sum(min(2 * minx, x) for x in last[0 : len(last) // 2])


# @lc code=end
