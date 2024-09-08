#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: Node) -> Node:
        from collections import deque
        if not root:
            return root
        queue = deque([root])

        while queue:
            number_of_nodes_at_current_level = len(queue)
            for i in range(number_of_nodes_at_current_level):
                node = queue.popleft()
                if i < number_of_nodes_at_current_level - 1:
                    node.next = queue[0]
                else:
                    node.next = None
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

        
# @lc code=end

