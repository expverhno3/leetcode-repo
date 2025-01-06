#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.q2 = deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.length += 1

    def pop(self) -> int:
        for _ in range(self.length - 1):
            self.q2.append(self.q.popleft())
        res = self.q.popleft()
        self.q2, self.q = self.q, self.q2
        self.length -= 1
        return res

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return self.length == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

