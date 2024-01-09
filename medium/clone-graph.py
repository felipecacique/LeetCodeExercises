# https://leetcode.com/problems/clone-graph/solutions/1792858/python3-iterative-bfs-beats-98-explained/

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
        # Solution 1: we will traverse the graph, pre-order, and while createng a new one, coping each node

        def Solution1(node):
            if not node:
                return None

            node_copy = Node(node.val, [])
            visited = set()

            def dfs(node, node_copy):
                if (
                    node.val in visited
                ):  # lets not visit the same node twice. Prevent loop
                    return node_copy

                visited.add(node.val)  # mask as visited

                for neighbor in node.neighbors:
                    mycopy = Node(neighbor.val, [])
                    node_copy.neighbors.append(
                        mycopy
                    )  # add the node copy to the neighbors list
                    # print(node_copy.neighbors[-1].val)
                    node_copy.neighbors[-1] = dfs(
                        neighbor, node_copy.neighbors[-1]
                    )  # also have to pass the last copied neighbor
                return node_copy

            node_copy = dfs(node, node_copy)

            visited = set()

            def dfs2(node_copy):
                # print(node_copy.val)

                if (
                    node_copy.val in visited
                ):  # lets not visit the same node twice. Prevent loop
                    return

                visited.add(node_copy.val)  # mask as visited

                if not node_copy:
                    return

                vals = []
                for neighbor in node_copy.neighbors:
                    vals.append(neighbor.val)
                    dfs2(neighbor)  # also have to pass the last copied neighbor
                print(vals)

            dfs2(node_copy)

            return node_copy

        return Solution1(node)
