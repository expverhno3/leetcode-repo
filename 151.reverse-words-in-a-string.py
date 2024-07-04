#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    #note: best solution I saw in leetcode, link: https://leetcode.com/problems/reverse-words-in-a-string/solutions/3666063/python-o-1-spatial-complexity/
    def reverseOneWord(self, s: list, debut: int, fin: int):
        """takes a list, reverse its order"""
        i = 0
        while i < (fin-debut)//2:
            s[debut+i],s[fin-1-i]=s[fin-1-i],s[debut+i]
            i+=1

    def deleteSpacesSeries(self, s: list):
        
        # this delete space in the end
        i = len(s)-1
        while i>=0 and s[i]==" ":
            s.pop()
            i-=1

        # delete space at the beginning, then i points to the beginning non-space word
        i = 0
        while i < len(s) and s[i]==" ":
            i+=1

        write_i = 0

        while i < len(s):
            if not (s[i-1]==s[i]==" "): # if not two space in series
                s[write_i] = s[i] # put not space word to the beginning
                write_i += 1
            i += 1


        for _ in range(len(s)-write_i):
            s.pop() # pop the garbage elements remaining in list



    def reverseWords(self, s: str) -> str:
        s = list(s)

        # reverse the entire string
        self.reverseOneWord(s, 0, len(s))

        i = 0
        motDebut = 0
        motFin = 0
        estMotFini = False

        while i < len(s):
            if s[i]==" ":
                if estMotFini:
                    self.reverseOneWord(s, motDebut, motFin+1)
                    estMotFini = False
            else:
                # basically find where the word begins
                if not estMotFini:
                    # found begin of the word
                    estMotFini = True
                    motDebut = i
                    motFin = i
                else:
                    # in the middle of the word
                    motFin += 1
            i+=1

        if estMotFini:
            # if string is not end with a space -> not knowing word ends in the previous while loop
            self.reverseOneWord(s, motDebut, motFin+1)

        # clean up space
        self.deleteSpacesSeries(s)

        return "".join(s)
    

    #note: MY SOLUTION
    # def reverseWords(self, s: str) -> str:
    #     start = -1
    #     end = -1
    #     word_list = []
    #     s += ' '
    #     for i, char in enumerate(s):
    #         if start == -1 and char != ' ':
    #             start = i
    #             end = i
            
    #         if start != -1 and char == ' ':
    #             end = i -1
    #             word_list.append((start, end+1))
    #             start = -1
    #             end = -1
        
    #     words = []
    #     while word_list:
    #         start, end = word_list.pop()
    #         words.append(s[start:end])
    #     return ' '.join(words)
                

        
# @lc code=end

