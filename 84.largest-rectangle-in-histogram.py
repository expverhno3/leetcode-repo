#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack should keep ascending order, save index
        stack = [-1]
        heights.append(0)  # make sure last bar is smallest
        res = 0  # init with small value
        
        for i in range(len(heights)):
            cur_height = heights[i]

            # if highest bar saved higher than current bar
            while cur_height < heights[stack[-1]]:

                # limiting height (because before i, all bars will be >= h, or they will be saved in stack)
                h = heights[stack.pop()] 

                # right boundary: (i-1), left boundary: (stack[-1])
                w = i - 1 - stack[-1] 

                res = max(res, h * w)
            # height[i] > height[stack[-1]]
            stack.append(i)

        return res


# @lc code=end
