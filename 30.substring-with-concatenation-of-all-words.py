#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List
"""
"barfoofoobarthefoobarman"\n["bar","foo","the"]

"wordgoodgoodgoodbestword"\n["word","good","best","good"]

"lingmindraboofooowingdingbarrwingmonkeypoundcake"\n["fooo","barr","wing","ding","wing"]
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # --- impl from https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/13658/easy-two-map-solution-c-java/comments/13959
        # from collections import Counter, defaultdict
        # wordBag = Counter(words)   # count the freq of each word
        # wordLen, numWords = len(words[0]), len(words)
        # totalLen, res = wordLen*numWords, []
        # for i in range(len(s)-totalLen+1):   # scan through s
        #     # For each i, determine if s[i:i+totalLen] is valid
        #     seen = defaultdict(int)   # reset for each i
        #     for j in range(i, i+totalLen, wordLen):
        #         currWord = s[j:j+wordLen]
        #         if currWord in wordBag:
        #             seen[currWord] += 1
        #             if seen[currWord] > wordBag[currWord]:
        #                 break
        #         else:   # if not in wordBag
        #             break    
        #     if seen == wordBag:
        #         res.append(i)   # store result
        # return res

        from collections import Counter, defaultdict

        # Create a frequency table for the given words
        word_frequency_table = Counter(words)
        
        # Calculate the length of a single word and the total number of words
        word_length = len(words[0])
        total_words = len(words)
        
        # Calculate the total length of the substring we're looking for
        total_length = word_length * total_words
        result = []

        # Iterate over the string, checking each possible substring
        for start_index in range(len(s) - total_length + 1):
            # Create a frequency table to track the words we've seen
            seen_words = defaultdict(int)
            
            # Check each word in the current substring
            for word_index in range(start_index, start_index + total_length, word_length):
                current_word = s[word_index:word_index + word_length]
                
                # If the current word is in the word frequency table, increment its count
                if current_word in word_frequency_table:
                    seen_words[current_word] += 1
                    
                    # If we've seen more instances of the current word than expected, break
                    if seen_words[current_word] > word_frequency_table[current_word]:
                        break
                else:
                    # If the current word is not in the word frequency table, break
                    break
            
            # If we've seen all the words we're looking for, add the start index to the result
            if seen_words == word_frequency_table:
                result.append(start_index)
        
        return result


        # --- my impl
        # NOTE: problem of this impl: if string's word length != word_length, segregation will be wrong and no word can be detected
        # from collections import Counter, defaultdict
        # words_freq_table = Counter(words)
        # cur_freq_table = defaultdict(int)
        # res = []

        # word_length, num_words = len(words[0]), len(words)

        # s_words = [s[i*word_length: (i+1)*word_length] for i in range(len(s) // word_length)]
        
        # left, right = 0, 0
        # print(s_words)
        # while right < len(s_words):
        #     if s_words[right] in words_freq_table:
        #         cur_freq_table[s_words[right]] += 1
        #     if right - left > num_words-1:
        #         if s_words[left] in words_freq_table:
        #             cur_freq_table[s_words[left]] -= 1
        #         left += 1
        #     if s_words[right] in words_freq_table:
        #         while cur_freq_table[s_words[right]] > words_freq_table[s_words[right]]:
        #             if s_words[left] in words_freq_table:
        #                 cur_freq_table[s_words[left]] -= 1
        #             left += 1
        #     if cur_freq_table == words_freq_table:
        #         res.append(left*word_length)
        #         print("append here")
        #     print(cur_freq_table, left, right)
        #     right += 1
        # return res
        
# @lc code=end

