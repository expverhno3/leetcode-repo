#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the linked list to the right by k steps.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            k (int): The number of steps to rotate.

        Returns:
            Optional[ListNode]: The new head of the rotated linked list.
        """
        if not head or k == 0:
            return head

        # Find the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Connect the tail to the head to form a circular linked list
        tail.next = head

        # Find the new tail node
        new_tail = head
        for _ in range(length - k % length - 1):
            new_tail = new_tail.next

        # Find the new head node
        new_head = new_tail.next

        # Break the circular linked list at the new tail
        new_tail.next = None

        return new_head       
        
# @lc code=end

