#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from typing import List
"""
- multiple word start from same cell
[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain","hklf", "hf"]

- meet "$" sign but not necessary end searching
[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m, n = len(board), len(board[0])

        MOVE = ((1,0), (-1, 0), (0, 1), (0, -1))

        self.trie = {}
        for word in words:
            node = self.trie
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word # indicate end
        print(self.trie)

        def _dfs(node:dict, pos, visited:set):
            visited.add(pos)
            row, col = pos
            ans = []
            if "$" in node:
                ans.append(node["$"])
                del(node["$"])
            for mi, ni in MOVE:
                row += mi
                col += ni
                if 0 <= row < m and 0 <= col < n and board[row][col] in node and (row, col) not in visited:
                    res = _dfs(node[board[row][col]], (row, col), visited)
                    ans.extend(res)
                    visited.remove((row, col))
                row -= mi
                col -= ni
            return ans
            
        res = [] 
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in self.trie:
                    word = _dfs(self.trie[char], (i,j), set())
                    res.extend(word)
        return res
                    
                    
            
            
            
# @lc code=end

