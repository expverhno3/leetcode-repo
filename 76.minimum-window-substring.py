#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        # build a map to count char frequency
        char_map = defaultdict(int)
        for char in t:
            char_map[char] += 1

        counter = len(t) # check how many chars are matched
        begin, end = 0, 0
        min_length = float("inf")
        head = 0

        # expand window by move "end"
        while end < len(s):
            if char_map[s[end]] > 0: # this char in "t"
                counter -= 1
            char_map[s[end]] -= 1 # if this char in `t` -> >= 0; if this char not in `t` -> <0
            end += 1

            while counter == 0: # all target chars were contained in this window, now shrink window
                if end - begin < min_length: # if window smaller, take this case
                    min_length = end - begin
                    head = begin
                if char_map[s[begin]] == 0:
                    counter += 1
                char_map[s[begin]] += 1
                begin += 1

        return "" if min_length == float("inf") else s[head : head + min_length]


# @lc code=end
