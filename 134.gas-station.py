#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
# @lc code=start

"""
[4,5,3,1,4]\n[5,4,3,4,2]
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # --- my impl: simulation, too slow O(n^2)
        # n = len(gas)
        # is_arrived = True
        # for start_idx in range(n):
        #     tank = gas[start_idx]
        #     for i in range(n):
        #         actual_idx = (i+start_idx) % n
        #         current_cost = cost[actual_idx]
        #         current_gain = gas[(actual_idx + 1) % n]
        #         tank -= current_cost
        #         if tank <= 0 and i != n-1:
        #             is_arrived = False
        #             break
        #         if (actual_idx + 1) % n != start_idx:
        #             tank += current_gain
        #         # print(f"at {actual_idx}, tank: {tank}\tcost: {current_cost}\tgain: {current_gain}")
        #     if is_arrived and tank >= 0:
        #         return start_idx
        #     is_arrived = True
        #     # print("-----")
        # return -1
        # --- optimization (from: https://leetcode.com/problems/gas-station/solutions/1706142/java-c-python-an-explanation-that-ever-exists-till-now/?source=vscode)
        global_sums = 0
        i = 0
        local_sums = 0
        start_idx = 0
        
        for gasi, costi in zip(gas, cost):
            tmp = gasi - costi 
            global_sums += tmp
            local_sums += tmp
            if local_sums < 0:
                local_sums = 0
                start_idx = i + 1
            i += 1
        return start_idx if global_sums >= 0 else -1

            

                
        
# @lc code=end

