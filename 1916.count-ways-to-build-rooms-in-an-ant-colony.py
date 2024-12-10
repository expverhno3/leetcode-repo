#
# @lc app=leetcode id=1916 lang=python3
#
# [1916] Count Ways to Build Rooms in an Ant Colony
#

# @lc code=start
from typing import List
import collections
import math

class Solution:
    """
    This class is used to count the number of ways to build rooms in an ant colony.

    The waysToBuildRooms method takes a list of integers as input, where the i-th
    element is the index of the room that the i-th ant is in. The method returns
    the number of ways to build rooms in the ant colony.

    The method uses a depth-first search (DFS) to traverse the graph of rooms and
    ants. It uses a dictionary to store the graph, where the key is the index of
    the room and the value is a list of indices of the rooms that need to be built first before builing this room.
    """
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(prevRoom):
            g[pre].append(cur)
            
        def dfs(cur):
            if not g[cur]:
                return 1, 1
            ans, l = 1, 0
            for nxt in g[cur]:
                tmp, r = dfs(nxt)
                ans = (ans * tmp * math.comb(l+r, r)) % MOD
                l += r
            return ans, l + 1
            
        return dfs(0)[0]
# @lc code=end

