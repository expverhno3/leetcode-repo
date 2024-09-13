#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        queens can only attack each other when they share a same diag/row/col, which means: if there's a queen at (x,y), then any position (p,q) that x-y == p-q or x+y == p + q is invalid
        """
        res = []
        def dfs(queens, xy_diff, xy_sum):
            """queens only save column position, and index of each element indicates row position"""
            p = len(queens) # let's say next queen should be placed at p-th row
            if len(queens) == n:
                res.append(queens[:])
                return
            else:
                for q in range(n):
                    if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                        dfs(queens + [q], xy_diff + [p-q], xy_sum+[p+q])
        dfs([],[],[])
        return len(res)


# @lc code=end

