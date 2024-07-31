#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next.next if slow and slow.next else None
        while slow and fast:
            if fast == slow:
                return True
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
        return False
# @lc code=end

