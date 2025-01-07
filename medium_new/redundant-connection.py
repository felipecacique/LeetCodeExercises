class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/redundant-connection/?envType=problem-list-v2&envId=graph
        # time o(n) space o(n)

        # Create adj list
        from collections import defaultdict
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # Do a dfs, as we find a cycle (node that is already in seen) we stop the dfs. Now the recursion with return and we add the nodes in an array of cycleNodes, in a post order. When we fing a node that is already in cycleNodes, it means that the cycle has endes, and we stop adding nodes to the cycleNodes.
        seen = set()
        nodesFromCycle = set()
        endCycle = [False]
        def dfs(parent, node):
            if node in seen: # cycle starts here
                nodesFromCycle.add(node)
                return
            seen.add(node)
            for neighbour in adj[node]:
                if neighbour == parent: continue
                dfs(node, neighbour)
                if nodesFromCycle: 
                    if node in nodesFromCycle: endCycle[0] = True # cycle ends here
                    if not endCycle[0]: nodesFromCycle.add(node) # while cycle has not ended, we add the nodes to the cycle in a post order fashion
                    return

        node = edges[0][0]
        dfs(None, node)

        # Find the last adge that is part of the cycle
        ans = []
        for i in range(len(edges)-1, -1, -1):
            n1, n2 = edges[i]
            if n1 in nodesFromCycle and n2 in nodesFromCycle:
                ans = edges[i]
                break

        return ans

        
