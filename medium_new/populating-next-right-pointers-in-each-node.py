"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # do dfs and keep an array with right nodes per each level, starting from the right
        nextNodes = {}
        def dfs(node, h):
            if not node:
                return
            
            if h in nextNodes:
                node.next = nextNodes[h]
            else:
                node.next = None

            dfs(node.right, h+1)
            dfs(node.left, h+1)

            nextNodes[h] = node
        
            return 

        dfs(root, 1)

        return root