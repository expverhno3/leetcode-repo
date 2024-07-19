#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
import collections
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #--- BFS implementation
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

    # --- DFS implementation
    # def serialize(self, root):
    #     # Initialize an empty list to store serialized node values
    #     ans = []

    #     # Define a depth-first search (DFS) function to serialize the tree
    #     def DFS(root):
    #         # Base case: If the current node is None, append "N" to represent null node
    #         if not root:
    #             ans.append("N")
    #             return

    #         # Append the value of the current node to the list
    #         ans.append(str(root.val))
            
    #         # Recursively serialize left and right subtrees
    #         DFS(root.left)
    #         DFS(root.right)

    #     # Call the DFS function to serialize the tree
    #     DFS(root)
        
    #     # Join the list elements into a string separated by commas and return
    #     return ",".join(ans) # pre-order string

    # def deserialize(self, data):
    #     # Split the serialized string into a list of node values
    #     value = data.split(",")
        
    #     root_index = 0

        # Define a DFS function to reconstruct the tree from serialized data
        # def DFS():
        #     nonlocal root_index
        #     # If the current value is "N", indicating a null node, return None
        #     if value[root_index] == "N":
        #         root_index += 1
        #         return None

        #     # Create a new TreeNode with the current value
        #     root = TreeNode(int(value[root_index]))
        #     root_index += 1
            
        #     # Recursively construct left and right subtrees
        #     root.left = DFS()
        #     root.right = DFS()
            
        #     return root

        # # Call the DFS function to deserialize the tree and return the root
        # return DFS()

    #--- MY Implementation: serialize with level-order, deserialize with relation of parent node and child node (2i+1 and 2i+2), not working in some cases
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return ''
    #     queue = deque([root])
    #     res = []

    #     while queue:
    #         for i in range(len(queue)):
    #             node = queue.popleft()
    #             # print(node)
    #             if isinstance(node, int):
    #                 res.append(node)
    #             else:
    #                 res.append(node.val)
    #                 if node.left:
    #                     queue.append(node.left)
    #                 else:
    #                     queue.append(-1)
    #                 if node.right:
    #                     queue.append(node.right)
    #                 else:
    #                     queue.append(-1)
    #     print(res)
    #     return ",".join([str(num) for num in res])
                    
        

    # def deserialize(self, data:str):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if not data:
    #         return None

    #     node_list = [int(numstr) for numstr in data.split(",")]
    #     num_nodes = len(node_list)

        
    #     def build_tree(root_index):
    #         if node_list[root_index] == -1:
    #             return None
    #         root = TreeNode(node_list[root_index])
            
    #         if root_index * 2 + 1 < num_nodes:
    #             root.left = build_tree(root_index*2 + 1)
    #         if root_index * 2 + 2 < num_nodes:
    #             root.right = build_tree(root_index*2 + 2)
    #         return root
        
    #     return build_tree(0)
            
        
            
            
            


            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

