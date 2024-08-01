#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            if cur.next:
                tmp = cur.next.next
                cur_next = cur.next
                cur.next.next = cur
                cur.next = tmp
                if prev:
                    prev.next = cur_next
                if not prev:
                    head = cur_next
            prev = cur
            cur = cur.next
        return head


# @lc code=end
