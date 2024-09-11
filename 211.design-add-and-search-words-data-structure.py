#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from collections import defaultdict
class WordDictionary:

    def __init__(self):
        self.prefix_dict = {}

    def addWord(self, word: str) -> None:
        tmp = self.prefix_dict
        for char in word:
            tmp = tmp.setdefault(char, {})
        tmp["*"] = True

    def _dfs(self, d, word):
        for i, c in enumerate(word):
            if c == ".":
                return any(self._dfs(d[w], word[i+1:]) for w in d.keys() if w != "*")
            else:
                if c not in d:
                    return False
                else:
                    d = d[c]
        return "*" in d
                    

    def search(self, word: str) -> bool:
        # --- impl based on: https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/59725/python-easy-to-follow-solution-using-trie/comments/415657
        return self._dfs(self.prefix_dict, word)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

