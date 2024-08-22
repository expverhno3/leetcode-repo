#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        #note: ans from others
        # https://leetcode.com/problems/validate-stack-sequences/solutions/3411416/beats-99-2-easy-solution/
        
        # keep push into stack until meets the one need to pop out
        stack = []
        popped_pointer = 0

        for element in pushed:
            stack.append(element)
            while stack != [] and stack[-1] == popped[popped_pointer]:
                stack.pop()
                popped_pointer += 1
            
        return stack == []

        #note
        # whole point is: "simulate" the process
        # basically keep pushing into stack, until we meet the element that needs to be pushed into "popped". Then keep popping. After that continue pushing element. we just need to know when to pop, so if this operation is viable, stack temporarily store numbers should be empty

# @lc code=end

