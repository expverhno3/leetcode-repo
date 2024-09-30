#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            if a < 0:
                while res and res[-1] > 0 and res[-1] < -a:
                    res.pop()
                if res:
                    if res[-1] < 0:
                        res.append(a)
                    elif res[-1] > -a:
                        continue
                    elif res[-1] == -a:
                        res.pop()
                else:
                    res.append(a)
            else:
                res.append(a)
        return res
            

        
# @lc code=end

