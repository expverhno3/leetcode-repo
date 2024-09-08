#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- AI solution
class BSTIterator:

    # Initialize the iterator with the root node of the BST
    def __init__(self, root: Optional[TreeNode]):
        # Use a stack to store nodes, allowing us to efficiently traverse the BST
        self.stack = []
        # Push the leftmost nodes of the BST onto the stack
        self._push_left(root)

    # Helper method to push the leftmost nodes of a subtree onto the stack
    def _push_left(self, node: TreeNode):
        # Continue pushing nodes onto the stack until we reach a leaf node
        while node:
            # Push the current node onto the stack
            self.stack.append(node)
            # Move to the left child of the current node
            node = node.left

    # Return the next node in the in-order traversal
    def next(self) -> int:
        # Pop the top node from the stack
        node = self.stack.pop()
        # Push the leftmost nodes of the right subtree onto the stack
        self._push_left(node.right)
        # Return the value of the current node
        return node.val

    # Check if there are more nodes in the in-order traversal
    def hasNext(self) -> bool:
        # If the stack is not empty, there are more nodes to traverse
        return len(self.stack) > 0

# --- my impl
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.arr = []
#         self._recur(root)
#         self.current_idx = 0
        
#     def _recur(self, root:TreeNode):
#         if not root:
#             return
#         self._recur(root.left)
#         self.arr.append(root.val)
#         self._recur(root.right)
#         return


#     def next(self) -> int:
#         self.current_idx += 1
#         return self.arr[self.current_idx-1]


#     def hasNext(self) -> bool:
#         return self.current_idx < len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

