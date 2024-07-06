#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        list_of_each_row = ['' for _ in range(numRows)]
        
        increase_flag = True
        row_idx = 0

        for char in s:

            list_of_each_row[row_idx]+=char

            if row_idx + 1 == numRows and increase_flag:
                increase_flag = False
            elif row_idx - 1 == -1 and not increase_flag:
                increase_flag = True
                
            if increase_flag:
                row_idx += 1
            else:
                row_idx -= 1
        
        return ''.join([row for row in list_of_each_row])
            
            
                
            
        
# @lc code=end

