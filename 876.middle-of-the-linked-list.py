#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        if head is None:
            return

        counter = 0
        while fast:
            
            fast = fast.next
            counter += 1
            if counter % 2 == 0:
                slow = slow.next

        return slow 
                
            
# @lc code=end

