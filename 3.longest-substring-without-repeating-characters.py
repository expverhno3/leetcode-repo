#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #note: use two pointer approach
        if not s:
            return 0
        left = 0
        right = 0
        max_len = 0
        char_index = {}
        string_len = len(s)
        
        while right < string_len:
            current_char = s[right]
            
            if current_char in char_index and char_index[current_char] >= left:
                left = char_index[current_char] + 1
            char_index[current_char] = right
            current_len = right - left + 1
            max_len = max(current_len, max_len)
            right += 1
        return max_len



        
        #note: naive trial
        # if not s:
        #     return 0
        
        # max_length = 1
        # current_length = 0
        # current_char = None
        # prev_chars = []
        # i = 0
        # start_idx = 0
        # while i < len(s):
        #     current_char = s[i]
        #     # print(current_length)
        #     # print(prev_chars)
        #     # print(current_char)
        #     if current_char in prev_chars:
        #         max_length = current_length if max_length < current_length else max_length
        #         current_length = 0
        #         start_idx += 1
        #         i = start_idx
        #         prev_chars = []
        #         continue
        #     else:
        #         current_length += 1
        #         prev_chars.append(current_char)
        #     max_length = current_length if max_length < current_length else max_length
        #     i += 1
        # return max_length

# @lc code=end

