#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # two pointers: one for reading, one for writing 
        """
        read_cur = head
        
        node_to_index_old = {}
        index_to_node_list_new = []
        
        counter = 0

        while read_cur:
            value = read_cur.val
            node_to_index_old[read_cur] = counter
            read_cur = read_cur.next
            counter += 1
            index_to_node_list_new.append(Node(value))
        
        num_nodes = len(index_to_node_list_new)
        read_cur = head
        counter = 0
        while read_cur:
            random = read_cur.random
            random_index = node_to_index_old[random] if random in node_to_index_old.keys() else None
            index_to_node_list_new[counter].random = index_to_node_list_new[random_index] if random_index is not None else random_index
            index_to_node_list_new[counter].next = index_to_node_list_new[counter + 1] if (counter+1) < (num_nodes-1) else None

            read_cur = read_cur.next
            counter += 1
        
        return index_to_node_list_new[0]
        """
        
        #note: use original node as key, use new copy node as value
        original_node_to_copy_node_table = {}

        #note: first run, create new nodes
        current = head
        while current:
            original_node_to_copy_node_table[current] = Node(current.val)
            current = current.next
        
        #note: second run, build the links
        current = head
        while current:
            original_node_to_copy_node_table[current].next = original_node_to_copy_node_table.get(current.next, None)
            original_node_to_copy_node_table[current].random = original_node_to_copy_node_table.get(current.random, None)
            current = current.next

        return original_node_to_copy_node_table.get(head, None)
    
        
        
      
# @lc code=end

# BEST ANSWER:
# def copyRandomList(self, head: 'Node') -> 'Node':
#     if not head:
#         return None
#     visited = {None: None}
#     curr = head
#     while curr:
#         if curr not in visited:
#             visited[curr] = Node(curr.val)
#         if curr.next not in visited:
#             visited[curr.next] = Node(curr.next.val)
#         if curr.random not in visited:
#             visited[curr.random] = Node(curr.random.val)
#         visited[curr].next = visited[curr.next]
#         visited[curr].random = visited[curr.random]
#         curr = curr.next
#     return visited[head]