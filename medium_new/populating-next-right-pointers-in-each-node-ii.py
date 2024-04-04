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
    def connect(self, root: 'Node') -> 'Node':
        # https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/?envType=study-plan-v2&envId=top-interview-150
        # do the bredth first search, accessing nodes in height level order, and then we point the one nodes to the next, in the same height
        if not root: return root 
        from collections import deque
        queue = deque()
        queue.append((root,1)) # (node,height)
        node_prev, h_prev = None, None
        while queue:
            node, h = queue.popleft()
            if h_prev == h: node_prev.next = node
            node_prev, h_prev = node, h
            if node and node.left: queue.append((node.left,h+1))
            if node and node.right: queue.append((node.right,h+1))
        return root

        