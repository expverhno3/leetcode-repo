#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#


# @lc code=start
class StockSpanner:

    # --- impl by: https://leetcode.com/problems/online-stock-span/solutions/168311/c-java-python-o-1/?source=vscode
    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

    # --- my impl
    # def __init__(self):
    #     self.idx = 0
    #     self._results = []

    # def next(self, price: int) -> int:
    #     res = 1
    #     pre_idx = self.idx
    #     if self.idx != 0:
    #         prev_res = self._results[-1]
    #         while prev_res[0] <= price and prev_res[2] != pre_idx:
    #             res += prev_res[1]
    #             pre_idx = prev_res[2]
    #             if pre_idx - 1 == -1:
    #                 break
    #             prev_res = self._results[pre_idx - 1]

    #     self._results.append((price, res, pre_idx))
    #     self.idx += 1

    #     return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
