#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            # when there's no node / 1 node
            return head

        def get_linked_list_length(head: Optional[ListNode]) -> int:
            cur = head
            res = 0
            while cur:
                res += 1
                cur = cur.next
            return res

        def split(head: Optional[ListNode], n: int):
            """split a linked list into two, first linked list has length n, return head of second linked list"""

            # 1(head) -> 2 -> 3
            # 1 -> 2(cur) -> 3(tmp)

            cur = head
            for _ in range(1, n):
                if cur:
                    cur = cur.next
                else:
                    break
            if not cur:
                return None
            tmp, cur.next = cur.next, None
            return tmp

        def merge(
            l1: Optional[ListNode], l2: Optional[ListNode], head: Optional[ListNode]
        ):
            """merge two linked list in ascending order, linked merged list to `head`, return tail node"""
            cur = head
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    cur = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    cur = l1
                    l1 = l1.next
            cur.next = l1 if l1 else l2
            while cur.next:
                cur = cur.next
            return cur

        llength = get_linked_list_length(head)
        dummy = ListNode()
        dummy.next = head
        l, r, tail = None, None, None
        interval = 1
        while interval < llength:
            tail, cur = dummy, dummy.next
            while cur:
                l = cur
                #NOTE: split == disconnect + move `n` steps forward
                r = split(l, interval)
                cur = split(r, interval)
                tail = merge(l, r, tail)
            interval *= 2
        return dummy.next


# @lc code=end
