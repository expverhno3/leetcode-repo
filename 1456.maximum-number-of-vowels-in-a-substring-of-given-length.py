#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        from collections import deque
        VOWEL = {'a', 'e', 'i', 'o', 'u'}
        q = deque()
        for i in range(k):
            if s[i] in VOWEL:
                q.append(i)
        max_count = len(q)
        for i in range(k, len(s)):
            if q and q[0] == i - k:
                q.popleft()
            if s[i] in VOWEL:
                q.append(i)
            max_count = max(max_count, len(q))
        return max_count


        
# @lc code=end

