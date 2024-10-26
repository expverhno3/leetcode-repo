#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        def dfs(cur_dict, res:List[str]):
            for key in cur_dict.keys():
                if len(res) == 3:
                    return
                if key == "*":
                    res.append(cur_dict[key])
                else:
                    dfs(cur_dict[key], res)
            return

        trie_tree = {}
        for product in products:
            d = trie_tree
            for char in product:
                if char in d:
                    d = d[char]
                else:
                    d[char] = {}
                    d = d[char]
            d["*"] = product
        res = []
        cur_dict = trie_tree
        tmp_res = []
        for char in searchWord:
            tmp_res.clear()
            if char in cur_dict:
                cur_dict = cur_dict[char]
                dfs(cur_dict=cur_dict, res=tmp_res)
            else:
                cur_dict = dict()
            res.append(tmp_res[:])
        return res
                    
                        
                
                
            
                
                
        
# @lc code=end

