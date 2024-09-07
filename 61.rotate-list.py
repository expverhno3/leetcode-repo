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
            # if the linked list is empty or k is 0, return the head
            return head

        node_counter = 0
        current_node = head
        while current_node:
            # count the number of nodes in the linked list
            node_counter += 1
            current_node = current_node.next

        total_nodes = node_counter
        if total_nodes == 1 or k % total_nodes == 0:
            # if there's only one node or the number of steps is a multiple of the number of nodes, return the head
            return head

        node_counter = 0
        current_node = head
        # move to the tail node of the new linked list
        for _ in range(total_nodes - (k % total_nodes) - 1):
            current_node = current_node.next
        new_tail = current_node
        new_head = current_node.next
        current_node = new_head
        new_tail.next = None
        while current_node.next:
            current_node = current_node.next
        current_node.next = head
        # link the end of the new linked list to the original head

        return new_head
        
        
# @lc code=end

