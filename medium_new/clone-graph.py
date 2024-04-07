"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # https://leetcode.com/problems/clone-graph/?envType=study-plan-v2&envId=top-interview-150
        
        if not node: return None

        seen = {} # to avoid cycle and store the reference to the nodeClone

        def cloneGraph(node):
            if node.val in seen: # we return the reference for the nodeClone that we have already created in previous iteractions
                return seen[node.val]
            
            nodeClone = Node(node.val)
            seen[node.val] = nodeClone # stores a reference for the nodeClone
            for neighbor in node.neighbors:
                nodeClone.neighbors.append(cloneGraph(neighbor))
            
            return nodeClone
        
        return cloneGraph(node)
