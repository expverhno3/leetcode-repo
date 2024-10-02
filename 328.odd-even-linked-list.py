#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            even_head = head.next
        else:
            return head
        even_cur = even_head
        odd_cur = head

        while True:
            if even_cur.next:
                odd_cur.next = even_cur.next
                odd_cur = odd_cur.next
                if odd_cur.next:
                    even_cur.next = odd_cur.next
                    even_cur = even_cur.next
                    
                else: # ends at odd node
                    even_cur.next = None
                    odd_cur.next = even_head
                    break
            else: # ends at even node
                odd_cur.next = even_head
                break

        return head

                
        
# @lc code=end

