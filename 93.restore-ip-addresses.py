#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def is_valid_s(s):
            return (0 < int(s) <= 255 and s[0] != '0') or (s[0] == '0' and int(s) == 0 and len(s) == 1)
        def dfs(s, path:List[int]):
            if not s or (len(path) == 4 and s):
                return
            else:
                if len(path) == 3 and is_valid_s(s):
                    path.append(s)
                    res.append(path[:])
                    path.pop()
                else:
                    if s[0] == '0':
                        path.append(s[0])
                        dfs(s[1:], path)
                        path.pop()
                    else:
                        for i in range(1, 4):
                            if is_valid_s(s[:i]):
                                path.append(s[:i])
                                dfs(s[i:], path)
                                path.pop()
                            else:
                                break
            return
        dfs(s, [])
        return ['.'.join(l) for l in res]
            
        
# @lc code=end

