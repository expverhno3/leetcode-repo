#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        pre_slow = None
        count = 0
        while fast:
            fast = fast.next
            count += 1
            if count == 2:
                count = 0
                pre_slow = slow
                slow = slow.next
        
        # now slow at node to be deleted
        if pre_slow is not None:
            pre_slow.next = slow.next
            return head
        else:
            return None
        
        
# @lc code=end

