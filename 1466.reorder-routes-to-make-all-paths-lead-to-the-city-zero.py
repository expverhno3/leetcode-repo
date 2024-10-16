#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(adjacent_list: List[List[int]], visited:List[bool], from_node:int):
            number_of_change = 0
            visited[from_node] = True

            for to_node in adjacent_list[from_node]:
                if not visited[abs(to_node)]:
                    number_of_change += dfs(adjacent_list, visited, abs(to_node)) + int(to_node > 0) # if connected from_node -> to_node: need reverse
            return number_of_change
        
        adjacent_list = [[] for _ in range(n)]

        for c in connections:
            f, t = c
            adjacent_list[f].append(t)
            adjacent_list[t].append(-f) # indicating reversed connection
        return dfs(adjacent_list, [False] * n, 0)
        
# @lc code=end

