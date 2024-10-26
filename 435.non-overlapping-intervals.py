#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        start2idx = {}
        for idx, interval in enumerate(intervals):
            start = interval[0]
            if start not in start2idx:
                start2idx[start] = idx
        starts = list(start2idx.keys())
        start_idx = 0
        next_start = starts[start_idx]
        max_start = max(starts)
        keep = 0
        while next_start <= max_start:
            cur_start = starts[start_idx]
            if cur_start >= next_start:
                next_start = intervals[start2idx[cur_start]][1]
                keep += 1
            start_idx += 1
        return len(intervals) - keep
        # start_dict = {}
        # for i in intervals:
        #     idx = i[0]
        #     if idx in start_dict:
        #         start_dict[idx].append(i[:])
        #     else:
        #         start_dict[idx] = [i[:]]
        # for k in start_dict.keys():
        #     start_dict[k].sort(key=lambda x: x[1])
        
        # keep = 0
        # k = min(list(start_dict.keys()))
        # while k in start_dict:
        #     k = start_dict[k][0][1]
        #     keep += 1
        # return len(intervals) - keep

            
        
# @lc code=end

