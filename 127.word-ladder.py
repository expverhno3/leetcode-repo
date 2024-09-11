#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from typing import List

"""
"a"\n"c"\n["a","c"]
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        if beginWord == endWord or endWord not in wordList:
            return 0

        n = len(beginWord)
        wordSet = set(wordList)

        letters = set('abcdefghijklmnopqrstuvwxyz')
        q = deque([(beginWord, 1)])

        while q:
            cur_word, num_transform = q.popleft()
            for i in range(n):
                for l in letters:
                    transformation = cur_word[:i] + l + cur_word[i+1:]
                    if transformation in wordSet:
                        q.append((transformation, num_transform + 1))
                        wordSet.remove(transformation)
                        if transformation == endWord:
                            return num_transform + 1
        return 0
                    

# @lc code=end

