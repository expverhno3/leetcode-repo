#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from typing import List

# ["What","must","be","acknowledgment","shall","be"]\n16
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def calculate_word_groups(words, maxWidth):
            word_groups = []
            current_group_length = 0
            group_start_index = 0
            for i, word in enumerate(words):
                current_group_length += len(word)
                if current_group_length > maxWidth:
                    current_group_length -= len(word) + 1
                    word_groups.append([group_start_index, i, current_group_length])
                    current_group_length = len(word)
                    group_start_index = i
                current_group_length += 1  # space
            if current_group_length != 0:
                word_groups.append([group_start_index, i+1, current_group_length-1])
            return word_groups

        word_groups = calculate_word_groups(words, maxWidth)
        print(word_groups)

        justified_lines = []
        for i in range(len(word_groups)):
            line = ''
            start, end = word_groups[i][0], word_groups[i][1]
            num_words_in_group = end - start
            word_group = words[start:end]
            num_spaces_between_words = num_words_in_group - 1
            total_available_spaces = maxWidth - word_groups[i][2] + num_spaces_between_words
            extra_spaces = total_available_spaces % num_spaces_between_words if num_spaces_between_words > 0 else 0
            spaces_between_words = total_available_spaces // num_spaces_between_words if num_spaces_between_words > 0 else 0
            spaces = []
            if i != len(word_groups) - 1:
                if num_spaces_between_words > 0:
                    for j in range(num_spaces_between_words):
                        if extra_spaces > 0:
                            spaces.append(" " * (spaces_between_words + 1))
                            extra_spaces -= 1
                        else:
                            spaces.append(" " * (spaces_between_words))
                    spaces.append('')
                else:
                    spaces.append(" " * total_available_spaces)
            else:
                for j in range(num_spaces_between_words):
                    spaces.append(" ")
                    total_available_spaces -= 1
                spaces.append(" " * total_available_spaces)
            for word, space in zip(word_group, spaces):
                line += word
                line += space
            justified_lines.append(line)

        return justified_lines



                    
                
                
        
# @lc code=end

