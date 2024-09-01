#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ROM2INT = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        INT2ROM = {val: key for key, val in ROM2INT.items()}
        values = list(INT2ROM.keys())
        res = ""
        i = len(values) - 1
        while i >= 0:
            val = values[i]
            times = num // val
            if times == 4:
                res += INT2ROM[val] + INT2ROM[values[i+1]]
            elif times == 9:
                res += INT2ROM[val] + INT2ROM[values[i+2]]
            elif times >= 5:
                times = num // values[i+1]
                num = num % values[i+1]
                res += INT2ROM[values[i+1]] * times
                continue
            else:
                res += INT2ROM[val] * times
            num = num % val
            i -= 2
        return res
                


# @lc code=end
