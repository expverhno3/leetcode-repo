#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse(head):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return
        
        fast = slow = head
        counter = 0
        while fast.next:
            fast = fast.next
            counter += 1
            if counter == 2:
                slow = slow.next
                counter = 0
        fast = slow.next
        slow.next = None
        reverse(head)
        
        res = -float('inf')
        while slow:
            pair_sum = slow.val + fast.val
            res = max(res, pair_sum)
            slow = slow.next
            fast = fast.next
        return res
            

            

# @lc code=end

