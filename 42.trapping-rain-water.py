#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    """
    problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    """
    def trap(self, height: List[int]) -> int:
        # to save water: high1 -> low -> high2 (high1 <= high2)
        highest = 0
        left_res = 0
        temp_res = 0
        for i in range(len(height)): #NOTE: iterate left to right, count cases like [1,0,2,0,3] (ascending order)
            current_height =height[i]
            if current_height >= highest: # NOTE: = sign here to count things like [2,0,2], don't use "=" in both cases (duplicate)
                left_res += temp_res # put temp result in final result
                temp_res = 0
                highest = current_height
                
            elif current_height < highest: #NOTE: assume current highest is the shorter part of the "sink"
                temp_res += highest - current_height
        
        temp_res = 0
        right_res = 0
        highest = 0
        for i in range(len(height)-1, -1, -1): #NOTE: count cases like [3,0,2,0,1] (decending order)
            current_height =height[i]
            if current_height > highest:
                right_res += temp_res
                temp_res = 0
                highest = current_height
                
            elif current_height < highest:
                temp_res += highest - current_height
        return left_res + right_res
            
                    

        
# @lc code=end

