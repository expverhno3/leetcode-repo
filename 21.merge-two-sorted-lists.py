#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        prev = head
        current = None
        while list1 and list2:
            if list1.val <= list2.val:
                current = ListNode(list1.val)
                list1 = list1.next
            elif list2.val < list1.val:
                current = ListNode(list2.val)
                list2 = list2.next
            prev.next = current
            prev = current
        if list2:
            prev.next = list2
        elif list1:
            prev.next = list1
        return head.next

                

# @lc code=end

