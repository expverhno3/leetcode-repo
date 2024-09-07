#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
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

        dummy = ListNode(0)
        dummy.next = head

        prevprev = dummy
        prev = head
        cur = head.next

        while cur:
            if cur and prev.val == cur.val:
                while cur and cur.val == prev.val:
                    cur = cur.next
                while prev != cur:
                    tmp = prev.next
                    prev.next = None
                    prev = tmp
                prevprev.next = prev
                if cur:
                    cur = cur.next
            else:
                prevprev = prev
                prev = cur
                cur = cur.next
            if cur:
                print(f"{cur.val}, {prev.val}, {prevprev.val}")
        return dummy.next

            
        


# @lc code=end

