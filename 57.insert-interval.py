#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Insert a new interval into a list of non-overlapping intervals

        The new interval is merged into the list of intervals if it overlaps with any intervals.
        If the new interval does not overlap with any intervals, it is simply added to the list

        :param intervals: List of non-overlapping intervals
        :param new_interval: Interval to be inserted into the list
        :return: List of non-overlapping intervals
        """
        left_intervals, right_intervals = [], []  # left and right are used to store the intervals that are to the left and right of newInterval
        merged_interval = [new_interval[0], new_interval[1]]  # merged_interval is used to store the merged interval

        for interval in intervals:
            # if the current interval is to the left of the newInterval, add it to the left list
            if interval[1] < new_interval[0]:
                left_intervals.append(interval)
            # if the current interval is to the right of the newInterval, add it to the right list
            elif interval[0] > new_interval[1]:
                right_intervals.append(interval)
            # if the current interval overlaps with the newInterval, merge them
            else:
                merged_interval[0] = min(interval[0], merged_interval[0])
                merged_interval[1] = max(interval[1], merged_interval[1])

        # return the merged list of intervals
        return left_intervals + [merged_interval] + right_intervals
            
        
# @lc code=end
