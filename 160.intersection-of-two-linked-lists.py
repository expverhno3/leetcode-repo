#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # need to use a unique set of one list, then check if there's same node in the other list
        node_table = set()
        cur = headA
        while cur:
            node_table.add(cur)
            cur = cur.next
        
        cur = headB
        while cur:
            if cur in node_table:
                return cur
            cur = cur.next
        
        return None

# @lc code=end

