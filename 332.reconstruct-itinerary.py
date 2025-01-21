#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
"""
[["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]
"""
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        number_ticket_used = len(tickets)
        from collections import defaultdict
        from2to = defaultdict(list)
        for t in tickets:
            from2to[t[0]].append([t[1], False])
        for k in from2to.keys():
            from2to[k].sort(key=lambda x: x[0])
        
        res = []
        path = ['JFK']
        # print(from2to)

        def backtracking(cur_pos):
            # print("current position", cur_pos)
            nonlocal res, from2to, number_ticket_used
            if number_ticket_used == 0:
                res = path.copy()
                return True
            possible_dests = from2to[cur_pos]
            prev_dest = None
            for i in range(len(possible_dests)):
                dest = possible_dests[i][0]
                if not possible_dests[i][1] and (not prev_dest or dest != prev_dest):
                    prev_dest = dest
                    from2to[cur_pos][i][1] = True
                    path.append(dest)
                    number_ticket_used -= 1
                    found = backtracking(dest)
                    if found:
                        return True
                    from2to[cur_pos][i][1] = False
                    number_ticket_used += 1
                    path.pop()
        backtracking('JFK')
        return res

# @lc code=end

