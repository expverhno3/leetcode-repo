#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from typing import List

"""
max recursion depth exceeds
[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]\n[3.0,4.0,5.0,6.0]\n[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

[["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]\n[3.0,0.5,3.4,5.6]\n[["x2","x4"]]
"""

class Solution:
    # --- AI impl
    def calcEquation(equations, values, queries):
        graph = {}
        for (a, b), value in zip(equations, values):
            graph.setdefault(a, {})[b] = value
            graph.setdefault(b, {})[a] = 1 / value
    
        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1
            if b in graph[a]:
                return graph[a][b]
            for neighbor in graph[a]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    temp = dfs(neighbor, b, visited)
                    if temp != -1:
                        return graph[a][neighbor] * temp
            return -1
    
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        return res

    # --- my impl: adj matrix
    # def calcEquation(
    #     self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    # ) -> List[float]:
    #     valid_vars = set([v for row in equations for v in row])
    #     vars2idx = {v: i for i, v in enumerate(valid_vars)}
    #     idx2var = {i: v for i, v in enumerate(valid_vars)}
    #     adj_list = [[0] * len(valid_vars) for _ in range(len(valid_vars))]

    #     for eq, val in zip(equations, values):
    #         var1, var2 = eq
    #         adj_list[vars2idx[var1]][vars2idx[var2]] = val
    #         adj_list[vars2idx[var2]][vars2idx[var1]] = 1 / val
        

    #     for i in range(len(valid_vars)):
    #         adj_list[i][i] = 1

    #     res = []

    #     def find_divide(idx1, idx2, prev_history:List=[]):
    #         nonlocal adj_list
    #         if adj_list[idx1][idx2] != 0:
    #             return adj_list[idx1][idx2]
    #         else:
    #             col_idx = 0
    #             mul2 = -1
    #             while mul2 == -1 and col_idx < len(valid_vars):

    #                 while col_idx < len(valid_vars) and (adj_list[idx1][col_idx] == 0 or col_idx in prev_history):
    #                     col_idx += 1
                    
    #                 if col_idx < len(valid_vars):
    #                     mul1 = adj_list[idx1][col_idx]
                    
    #                 else:
    #                     return -1

    #                 prev_history.append(col_idx)
    #                 mul2 = find_divide(col_idx, idx2, prev_history[:])
    #             adj_list[idx1][idx2] = mul1 * mul2 if mul2 > 0 else -1
    #             return adj_list[idx1][idx2]

    #     for q in queries:
    #         var1, var2 = q
    #         if var1 in valid_vars and var2 in valid_vars:
    #             res.append(find_divide(vars2idx[var1], vars2idx[var2],[]))
    #         else:
    #             res.append(-1)
    #     return res


# @lc code=end
