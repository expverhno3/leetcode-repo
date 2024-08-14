#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        from heapq import heappushpop, heappush
        
        class MyItem:
            def __init__(self, item):
                self.key = item[0]
                self.value = item[1]
            
            def __lt__(self, other):
                return self.value < other.value
                

        hash_table = defaultdict(int)

        for num in nums:
            hash_table[num] += 1
        
        items = hash_table.items()
        heap = []
        for item in items:
            # item is (key, value)
            item = MyItem(item)
            if len(heap) < k:
                heappush(heap, item)
            else:
                heappushpop(heap, item)
        
        return [item.key for item in heap]
                
# @lc code=end

