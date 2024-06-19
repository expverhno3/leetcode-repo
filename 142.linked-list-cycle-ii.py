#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = head
        slow = head

        while fast:
            
            if fast.next is None:
                return None

            if fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None

            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

        # node_set = set()
        # current = head
        # while current:

        #     if current not in node_set:
        #         node_set.add(current)
        #     else:
        #         break
            
        #     current = current.next
        
        # return current

# @lc code=end

