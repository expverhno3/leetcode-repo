#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        dummy = ListNode()
        cur = dummy
        heap = []
        for i, l in enumerate(lists):
            heapq.heappush(heap, (l.val, i))
        while heap:
            val, list_idx = heapq.heappop(heap)
            node = lists[list_idx]
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx))
                lists[list_idx] = node.next
        return dummy.next
        

            
        
# @lc code=end

