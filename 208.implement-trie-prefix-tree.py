#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        from collections import defaultdict
        self.full_words = set()
        self.starts_with_dict = {}
        

    def insert(self, word: str) -> None:
        self.full_words.add(word)
        tmp = self.starts_with_dict
        for char in word:
            if char not in tmp:
                tmp[char] = {}
            tmp = tmp[char]
        

    def search(self, word: str) -> bool:
        return word in self.full_words
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.starts_with_dict
        for c in prefix:
            if c in tmp:
                tmp = tmp[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

