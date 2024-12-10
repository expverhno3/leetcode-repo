from typing import List


"""
problem: there are `n` cities, and connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is cost_i

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1
"""

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # from https://leetcode.com/problems/connecting-cities-with-minimum-cost/solutions/376079/python-prim-s-and-kruskal-s-algorithm-with-comments/?envType=problem-list-v2&envId=minimum-spanning-tree
        '''
        Kruskal's Algorithm:
        1) Create a forest F (a set of trees), where each vertex in 
        the graph is a separate tree.
        2) Create a set S containing all the edges in the graph.
        3) While S is nonempty and F is not yet spanning (fully connected):
            3A) Remove an edge with minimum weight from S
            3B) If the removed edge connects two different trees then 
            add it to the forest F, combining two trees into a single tree.
        '''
        def find(city):
            """
            find the root of the tree (where parent[node] == node)
            """
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        def union(c1, c2):
            """
            get root of two nodes, compare
                if they are from same root: return False (add this edge will cause cycle)
                if they are from differnt root: return True (yes! we connect two different trees)
            no matter what, root1 will be parent of root2
            """
            root1, root2 = find(c1), find(c2)
            if root1 == root2:
                return False # they are in the same tree
            parent[root2] = root1  # Always join roots!
            print(f"==> {parent}")
            return True
        
        # [1] Keep track of disjoint sets. Initially each city is its own set.
        parent = {city: city for city in range(1, n+1)}
        # [2] Sort connections so we are always picking minimum cost edge.
        connections.sort(key=lambda x: x[2])
        total = 0
        for city1, city2, cost in connections:  # [3A]  
            # assume city1 -> city2, then city1 is parent node of city2
            if union(city1, city2):  # [3B]
                total += cost
        # Check that all cities are connected.
        root = find(n)
        return total if all(root == find(city) for city in range(1, n+1)) else -1        
Solution().minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]])