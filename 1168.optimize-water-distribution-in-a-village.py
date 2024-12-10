
class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        consider wells as cost from house0 to all other houses -> unify the formulation (just consider cost)
        from: https://leetcode.com/problems/optimize-water-distribution-in-a-village/solutions/365853/c-python-java-hidden-well-in-house-0/?envType=problem-list-v2&envId=minimum-spanning-tree
        """
        parent = {i: i for i in range(n + 1)}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        w = [[c, 0, i] for i, c in enumerate(wells, 1)]
        p = [[c, i, j] for i, j, c in pipes]
        res = 0
        for c, x, y in sorted(w + p):
            rootx, rooty = find(x), find(y)
            if x != y: # do merge
                parent[rootx] = rooty
                res += c
                n -= 1
            if n == 0:
                return res
