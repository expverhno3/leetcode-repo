#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev_val = head.val
        prev = head
        cur = head.next
        while cur:
            if cur.val == prev_val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev_val = cur.val
                prev = cur
                cur = cur.next
        return head
# @lc code=end

