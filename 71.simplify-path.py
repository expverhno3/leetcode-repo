#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = [d for d in path.split('/') if d]
        res = []
        for d in dirs:
            res.append(d)
            if d == ".":
                res.pop()
            elif d == "..":
                res.pop()
                if res:
                    res.pop()
        return "/" + "/".join(res)
                
            

        

# @lc code=end

