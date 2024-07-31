#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def create_node_and_link(current:ListNode, full_sum):
            if full_sum >= 10:
                current.next = ListNode(full_sum % 10)
                carry = 1
            else:
                current.next = ListNode(full_sum)
                carry = 0
            return current, carry


        carry = 0
        cur1, cur2 = l1, l2
        head = ListNode()
        cur = head
        while cur1 or cur2:
            if cur1 and cur2:
                full_sum = cur1.val + cur2.val + carry
                cur, carry = create_node_and_link(cur, full_sum)
                cur = cur.next
                cur1 = cur1.next
                cur2 = cur2.next
            else:
                if not cur1:
                    full_sum = cur2.val
                    cur2 = cur2.next
                else:
                    full_sum = cur1.val
                    cur1 = cur1.next
                full_sum += carry
                cur, carry = create_node_and_link(cur, full_sum)
                cur = cur.next
        if carry == 1:
            cur.next = ListNode(1)
        return head.next
                
                
                
                    
        
        
# @lc code=end

