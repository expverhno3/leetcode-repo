#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #NOTE: move slow to one node before the node to be deleted, fast to the `None` tail
        # slow -> nth -> ... -> tail -> None (fast)
        slow = head
        fast = slow
        for _ in range(n+1):
            if fast:
                fast = fast.next
            else:
                # not enough space, remove slow itself
                return slow.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        
        
        
# @lc code=end

