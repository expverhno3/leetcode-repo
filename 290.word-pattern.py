#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        from collections import defaultdict

        pattern_pos = defaultdict(list)
        for i, c in enumerate(pattern):
            pattern_pos[c].append(i)
        
        s_words = s.split(" ")
        if len(s_words) != len(pattern):
            return False
        used = set()
        
        for key in pattern_pos:
            pos_list = pattern_pos[key]
            prev = s_words[pos_list[0]]
            if prev not in used:
                used.add(prev)
            else:
                return False
            for i in range(1, len(pos_list)):
                if s_words[pos_list[i]] != prev:
                    return False
        return True
                
            

        
# @lc code=end

