#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # optimized with matching
        res = []

        def dfs(idx,path):
            if (len(s) == idx):
                res.append(' '.join(path))
                
            for i in range(idx,len(s)):   
                tmp = s[idx:i+1]
                if (tmp in wordDict):
                    dfs(i+1,path+[tmp])

        dfs(0,[])
        return res 

        # --- init attempt, passed, backtracking ---
        # res = []
        # word2idx = {word: idx for idx,word in enumerate(wordDict)}
        # max_word_length = max([len(word) for word in wordDict])
        # tmp_res = []
        # def dfs(left):
        #     if left == len(s):
        #         res.append(tmp_res[:])
        #         return True
        #     for i in range(left+1, len(s)+1):
        #         cur_word = s[left: i]
        #         # print(cur_word)
        #         if cur_word in word2idx:
        #             tmp_res.append(word2idx[cur_word])
        #             dfs(i)
        #             tmp_res.pop()
        #         else:
        #             if len(cur_word) > max_word_length:
        #                 break
        #     return False
        # dfs(0)
        # if not res:
        #     return res
        # else:
        #     out = []
        #     for r in res:
        #         r = [wordDict[wordidx] for wordidx in r]
        #         out.append(' '.join(r)) 
        #     return out
                    
                    

        
# @lc code=end

