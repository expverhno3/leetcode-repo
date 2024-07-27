#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # --- Implementation from leetcode, using hash map (dictionary)
        # init
        char_freqs, indices, len_p, len_s = defaultdict(int), [], len(p), len(s)
        
        # s cannot have p anangrams if len(p) > len(s)
        if len_p > len_s:
            return indices

        # build map of character frequencies in p
        for char in p:
            char_freqs[char] += 1

        # initial full pass over the window, except last element which we will pass over later
        for i in range(len_p - 1):
            if s[i] in char_freqs:
                char_freqs[s[i]] -= 1
            
        # slide the window with stride 1, adding the value "sliding out" and subtracting the value "sliding in"
        for i in range(-1, len_s - len_p + 1):
            if i > -1 and s[i] in char_freqs:
                char_freqs[s[i]] += 1
            if i + len_p < len_s and s[i + len_p] in char_freqs: 
                char_freqs[s[i + len_p]] -= 1
                
            # check whether we encountered an anagram by seeing if all frequencies add up to 0
            if not any(char_freqs.values()): 
                indices.append(i + 1)
                
        return indices


        # --- MY IMPLEMENTATION (HASH VALUE)
        # window_width = len(p)
        # hash_val = sum([hash(char) for char in p])
        # res = []
        # for i in range(0, len(s) - window_width + 1):
        #     temp_hash = sum([hash(char) for char in s[i: i+window_width]])
        #     if temp_hash == hash_val:
        #         res.append(i)
        # return res
                

        
# @lc code=end

