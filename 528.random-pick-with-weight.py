#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        prefix_sum = [w[0]]
        self.intervals = [(1, prefix_sum[0])]
        for i in range(1, len(w)):
            prefix_sum.append(prefix_sum[-1] + w[i])
            self.intervals.append((prefix_sum[-2] + 1, prefix_sum[-1]))

    def pickIndex(self) -> int:
        rand_int = random.randint(1, self.intervals[-1][1])
        left = 0
        right = len(self.intervals)

        while left <= right:
            mid = (left + right) // 2
            i = self.intervals[mid]
            if i[0] <= rand_int <= i[1]:
                return mid
            elif i[0] > rand_int:
                right = mid - 1
            else:
                left = mid + 1
        return 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
