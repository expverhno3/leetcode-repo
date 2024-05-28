#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        #note: this based on leetcode solution

        # NUMBER = "1234567890"
        # curNum = 0
        # curString = ''
        # stack = []
        # for char in s:
        #     if char in NUMBER:
        #         curNum = curNum*10 + int(char)
        #     elif char == '[':
        #         stack.append(curString)
        #         stack.append(curNum)
        #         curString = ''
        #         curNum = 0
        #     elif char == ']':
        #         num = stack.pop()
        #         prevString = stack.pop()
        #         curString = prevString + curString * num
        #     else:
        #         curString += char
        # return curString



        #note: my solution
        NUMBER = "1234567890"
        number_before_bracket = []
        num_string_before_bracket = []
        counter = 0
        prefix = ''
        prefix_stack = []
        while counter < len(s):
            char = s[counter]
            if char in NUMBER:
                num_string_before_bracket.append(char)
            elif char == '[':
                prefix_stack.append(prefix)
                prefix = ''
                number_before_bracket.append(int(''.join(num_string_before_bracket)))
                num_string_before_bracket = []
            elif char == ']':
                if prefix:
                    prefix = number_before_bracket.pop() * prefix
                if prefix_stack:
                    prefix = prefix_stack.pop() + prefix
            else:
                prefix += char
            counter += 1
        return prefix

                        


# @lc code=end

