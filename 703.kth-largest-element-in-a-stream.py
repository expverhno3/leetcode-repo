#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
from typing import List
from heapq import heappush, heappushpop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for i in range(len(nums)):
            num = nums[i]
            if i < k:
                heappush(self.h, num)
            else:
                heappushpop(self.h, num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heappush(self.h, val)
        else:
            heappushpop(self.h, val)
        return self.h[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

