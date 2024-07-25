#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        value2idx = {}
        for i in range(len(strs)):
            s = strs[i]
            if not s:
                if -1 not in value2idx:
                    value2idx[-1] = [s]
                else:
                    value2idx[-1].append(s)
                continue
            value = sum([hash(char) for char in s])
            if value not in value2idx:
                value2idx[value] = [s]
            else:
                value2idx[value].append(s)
        print(value2idx.keys())
        return [value2idx[value] for value in value2idx.keys()]
# @lc code=end

