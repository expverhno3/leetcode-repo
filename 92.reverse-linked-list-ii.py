#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
"""[3,5]\n1\n2"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_list(head: Optional[ListNode], num_nodes: int) -> Optional[ListNode]:
            """
            Reverse a linked list with num_nodes nodes.

            Args:
                head: the head of the linked list
                num_nodes: the number of nodes in the linked list

            Returns:
                the new head of the reversed linked list
            """
            prev_node = head
            current_node = prev_node.next
            for _ in range(num_nodes):
                # keep track of the current node and the previous node
                temp = prev_node
                prev_node = current_node
                current_node = current_node.next
                # reverse the link
                prev_node.next = temp
            # link the end of the reversed list to the original list
            head.next = current_node
            return prev_node
        
        if left == right:
            return head

        current_node = head
        dummy = ListNode() # dump node
        previous_node = dummy
        dummy.next = head

        counter = 1
        while counter < left:
            current_node, previous_node = current_node.next, current_node
            counter += 1
        
        previous_node.next = reverse_list(current_node, right - left)

        return dummy.next




# @lc code=end

