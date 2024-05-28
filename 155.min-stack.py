#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            # always keep first value pushed into stack
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] >= val:
                # please note the "=" here! used to keep multiple same min value
                self.min_stack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            # if min stack needs to pop together
            self.min_stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

