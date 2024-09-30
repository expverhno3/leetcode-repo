#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        
        # --- stack!!!
        res = []
        for char in s:
            if char == "*":
                res.pop()
            else:
                res.append(char)
        return "".join(res)


        # --- init impl: back iteration, use hash table to mark chars that should be deleted
        # slow = fast = len(s) - 1
        # no_visit_set = set()
        # res = []
        # while slow >= 0:
        #     char  = s[slow]
        #     if char == "*" and slow - 1 >= 0:
        #         while (fast >= slow or s[fast] == "*") and fast >= 0:
        #             fast -= 1
        #         if fast >= 0 and s[fast] != "*":
        #             no_visit_set.add(fast)
        #             fast -= 1
        #     elif slow in no_visit_set:
        #         pass
        #     elif slow not in no_visit_set:
        #         res.append(char) 
        #     slow -= 1
        # return "".join(res[::-1])
                
        
# @lc code=end

