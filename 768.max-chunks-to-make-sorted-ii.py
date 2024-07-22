#
# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#

# @lc code=start
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        head_stack = [] # need to be ascending
        
        for num in arr:
            if head_stack and num < head_stack[-1]:
                head = head_stack.pop()
                while head_stack and num < head_stack[-1]: # if new number is smaller than previous head -> need to combine previous subarrays
                    head_stack.pop()
                head_stack.append(head)
            else:
                head_stack.append(num)
        return len(head_stack)


# @lc code=end
