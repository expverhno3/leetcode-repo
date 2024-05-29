#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heappushpop, heappush, heappop
class MedianFinder:
    def __init__(self) -> None:
        self.smaller_heap, self.larger_heap = [], []
        self.is_even = True
    
    def addNum(self, value):
        #note: heapq lib consider heap as min heap by default
        if self.is_even:
            heappush(self.larger_heap, -heappushpop(self.smaller_heap, -value))
        else:
            heappush(self.smaller_heap, -heappushpop(self.larger_heap, value))
        self.is_even = not self.is_even
    
    def findMedian(self):
        if self.is_even:
            return (self.larger_heap[0] + (-self.smaller_heap[0])) / 2
        else:
            return self.larger_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

"""
overview: use two heaps to find median.

1. what is heap:
    - min heap: parent node is always < any child node, top of heap is the MIN value of the heap
    - max heap: parent node is always > any child node, top of heap is the MAX value of the heap
2. why heap:
    - maintain two "container" with elements sorted
    - easy to get the MAX or MIN value
3. how this problem solved:
    - median: (MAX of the smaller half + MIN of the larger half) / 2
    - two heaps: max heap for smaller half and min heap for larger half
    - addNumber:
        - # of nodes: (k, k) -> (k, k+1); (k, k+1) -> (k+1, k+1)
        - how to keep two heaps sorted when a new number is added (take case 1 as example, new value as `x`, larger heap as `l`, smaller heap as `s`):
            - push x into l, then pop out a MIN value in l (as y)
            - push y into s, then pop out a MAX value in s (as z)
            - again, push z into l, so two heaps together are sorted!
    - findMedian:
        - two heaps have same number of nodes: use two top number
        - larger heap have more nodes: use this top number
"""


#note: too slow!!
# class MedianFinder:

#     def __init__(self):
#         self.is_even = True
#         self.stack = []
#         self.stack_len = 0
    

#     def addNum(self, num: int) -> None:

#         self.stack.append(num)
#         self.is_even = not self.is_even
#         self.stack_len += 1

#         for i in range(self.stack_len-1, 0, -1):        
#             if self.stack[i] <= self.stack[i-1]:
#                 self.stack[i], self.stack[i-1] = \
#                 self.stack[i-1], self.stack[i]
#             else:
#                 break



#     def findMedian(self) -> float:
#         if not self.is_even:
#             return self.stack[int((self.stack_len - 1)/2)]
#         else:
#             return (self.stack[int(self.stack_len / 2)] + self.stack[int(self.stack_len / 2)-1]) / 2