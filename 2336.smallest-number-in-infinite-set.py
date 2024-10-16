#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
from heapq import heappop, heappush

class SmallestInfiniteSet:

    def __init__(self):
        self._back_heap = []
        self._back_heap_set = set()
        self._previous_not_back_num = 0

    def popSmallest(self) -> int:
        if self._back_heap:
            num = heappop(self._back_heap)
            self._back_heap_set.remove(num)
            return num
        else:
            self._previous_not_back_num += 1
            return self._previous_not_back_num

    def addBack(self, num: int) -> None:
        if num not in self._back_heap_set and num > 0 and num <= self._previous_not_back_num:
            heappush(self._back_heap, num)
            self._back_heap_set.add(num)
            return
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

