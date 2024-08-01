#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
from  typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head:Optional[ListNode]) -> Optional[ListNode]:
            """given head of linked list, reverse and return its new head"""
            cur = head
            prev = None
            cur_next = cur.next
            while cur_next:
                tmp = cur_next.next
                cur_next.next = cur
                cur.next = prev
                prev = cur
                cur = cur_next
                cur_next = tmp
            return cur

        def pointer_move(current, steps):
            """move to group end"""
            if not current:
                return None
            for _ in range(steps):
                if current.next:
                    current = current.next
                else:
                    return None
            return current
                
        steps = k-1
        cur = head
        end = pointer_move(cur, steps)
        prev = None
        while end:
            tmp = end.next
            end.next = None
            group_head = reverse(cur)
            if prev:
                prev.next = end
            else:
                res = end
            prev = cur
            cur = tmp
            end = pointer_move(cur, steps)
        prev.next = cur
        return res
            

            

                       
# @lc code=end

