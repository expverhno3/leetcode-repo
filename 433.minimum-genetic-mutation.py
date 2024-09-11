#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
"""
"AACCGGTT"\n"AAACGGTA"\n["AACCGGTA","AACCGCTA","AAACGGTA"]
"""
from typing import List
from collections import deque
from itertools import product
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        # --- impl by https://leetcode.com/problems/minimum-genetic-mutation/solutions/189662/python-bfs-same-as-word-ladder/comments/1180700
        if startGene == endGene:
            return 0

        n, bank = len(startGene), set(bank)
        q = deque([(startGene, 0)])

        while q:
            cur, level = q.popleft()

            for i, g in product(range(n), 'ACGT'):
                mutation = cur[:i] + g + cur[i + 1:]

                if mutation in bank:  # unvisited
                    if mutation == endGene:
                        return level + 1

                    bank.remove(mutation)
                    q.append((mutation, level + 1))

        return -1


        
# @lc code=end

