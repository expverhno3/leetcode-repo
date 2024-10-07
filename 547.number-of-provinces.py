#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from collections import deque
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        number_of_groups = 0
        current_group = deque()

        
        for i in range(n):
            if i in visited:
                continue
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    current_group.append(j)
            visited.add(i)
            while current_group:
                next_node = current_group.popleft()
                visited.add(next_node)
                for k in range(n):
                    if isConnected[next_node][k] == 1 and k not in current_group and k not in visited:
                        current_group.append(k)
            number_of_groups += 1
            current_group.clear()
        return number_of_groups

            
            
                
                

                    



# @lc code=end

