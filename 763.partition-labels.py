#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # build table
        end_dict = {char:i for i, char in enumerate(s)}
        
        # partition
        res = []
        right_boundary_of_partition = -1
        left_boundary_of_partition = 0
        for i, char in enumerate(s):
            right_boundary_of_partition = max(right_boundary_of_partition, end_dict[char])

            if i == right_boundary_of_partition:
                res.append(right_boundary_of_partition - left_boundary_of_partition + 1)
                left_boundary_of_partition = i+1
        
        return res

        
# @lc code=end

