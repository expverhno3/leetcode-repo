#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_list_head = ListNode()
        ge_list_head = ListNode()
        
        cur = head
        less_list_pointer = less_list_head
        ge_list_pointer = ge_list_head
        while cur:
            
            if cur.val < x:
                less_list_pointer.next = cur
                less_list_pointer = less_list_pointer.next
            else:
                ge_list_pointer.next = cur
                ge_list_pointer = ge_list_pointer.next
            cur = cur.next
        ge_list_pointer.next = None
        less_list_pointer.next = ge_list_head.next
        return less_list_head.next


# @lc code=end

