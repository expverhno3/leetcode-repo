#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # from https://leetcode.com/problems/dota2-senate/solutions/3483399/simple-diagram-explanation/?source=vscode
        r_queue = deque()
        d_queue = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        next_pos = len(senate)
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(next_pos)
            else:
                d_queue.append(next_pos)
            next_pos += 1
        return "Radiant" if r_queue else "Dire"
# @lc code=end

