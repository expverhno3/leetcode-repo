#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from typing import List
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        to_visit = deque(rooms[0])
        visited = set([0])
        
        while to_visit:
            this_room = to_visit.popleft()
            visited.add(this_room)
            keys_in_this_room = rooms[this_room]
            for key in keys_in_this_room:
                if key not in to_visit and key not in visited:
                    to_visit.append(key)
        
        return len(visited) == len(rooms)
                    
        
# @lc code=end

