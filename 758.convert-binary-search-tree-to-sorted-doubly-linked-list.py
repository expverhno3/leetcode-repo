class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:

    def convertBST2DoubleLinkList(self, root: TreeNode) -> List[int]:
        #NOTE: (left -> parent), (right -> successor)
        
        def dfs(root: TreeNode):
            # depth first traverse (in-order)

            if root is None:
                return
            nonlocal prev, head
            dfs(root.left)

            if prev:
                prev.right = root
                root.left = prev
            else:
                # arrive at leftmost node, it's head
                head = root
            prev = root
            dfs(root.right)
            
        

        if root is None:
            return None
        
        head = prev = None

        dfs(root)

        # after connecting all prev nodes, `prev` points to last node
        prev.right = head
        head.left = prev
        
        return head
