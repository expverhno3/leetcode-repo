#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        res = 0

        prev = chars[0]
        start = 0
        counter = 0
        for char in chars:
            if char != prev:
                res += 1
                chars[start] = prev
                if counter > 1:
                    res += len(list(str(counter)))
                    tmp = list(str(counter))
                    chars[start+1:start+1+len(tmp)] = tmp[:]
                    start = start + 1 + len(tmp)
                else:
                    start += 1
                counter = 1
            else:
                counter += 1
            
            prev = char
        
        res += 1
        chars[start] = prev
        if counter > 1:
            res += len(list(str(counter)))
            tmp = list(str(counter))
            chars[start+1:start+1+len(tmp)] = tmp[:]
        return res
        
# @lc code=end

