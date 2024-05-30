#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        """more efficient way to solve.
        """
        s2t, t2s = {}, {}
        
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char in s2t and s2t[s_char] != t_char:
                return False
            if t_char in t2s and t2s[t_char] != s_char:
                return False
            
            s2t[s_char] = t_char
            t2s[t_char] = s_char
        return True
                

    def isIsomorphic1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_dict = {}
            t_dict = {}
            for i in range(len(s)):
                if s[i] not in s_dict:
                    s_dict[s[i]] = [i]
                else:
                    s_dict[s[i]].append(i)
                if t[i] not in t_dict:
                    t_dict[t[i]] = [i]
                else:
                    t_dict[t[i]].append(i)
        s_keys = list(s_dict.keys())
        t_keys = list(t_dict.keys())
        if len(s_keys) != len(t_keys):
            return False
        else:
            for i, skey in enumerate(s_keys):
                if s_dict[skey] != t_dict[t_keys[i]]:
                    return False
            return True

                

        
# @lc code=end

