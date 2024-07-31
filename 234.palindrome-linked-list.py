#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # --- impl from: https://leetcode.com/problems/palindrome-linked-list/solutions/1137027/js-python-java-c-easy-floyd-s-reversal-solution-w-explanation/

        # NOTE use fast & slow pointers + reverse linked list
        slow, fast, prev = head, head, None

        # fast's stride is 2, slow's is 1
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # stop when fast's next or fast's next next node doesn't exist
        # if odd nodes: [1,2,3,4,5], fast: 1->3->5, slow: 1->2->3
        # if even nodes: [1,2,3,4,5,6], fast: 1->3->5, slow: 1->2->3

        # keep moving slow forward, and reverse remaining linked list (slow.next as tail node of reversed linked list)
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # here `prev` at original tail node
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True


# @lc code=end
