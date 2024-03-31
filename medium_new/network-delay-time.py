class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # https://leetcode.com/problems/network-delay-time/
        
        node_time = [float('inf')] * n
        
        # create an adjacency list
        adj = {}
        ws = {}
        for time in times:
            if not time[0] in adj: 
                adj[time[0]] = []
            adj[time[0]].append(time[1])
            ws[(time[0], time[1])] = time[2]
        
        # traverse the graph
        visited = set()
        def dfs(node, t):
            
            if node in visited and t >= node_time[node-1]:  # we might visit the node again only if  t < node_time[node-1], so if we there is apath that reaches it faster than the previous
                return
            
            visited.add(node)
            
            if not node in adj:
                node_time[node-1] = t
                return
            
            node_time[node-1] = t
            
            for neighbour in adj[node]:
                dfs(neighbour, t + ws[(node,neighbour)])
        
        dfs(k, 0)
        
        if float('inf') in node_time: # the signal did not reach all nodes
            return -1
        
        return max([-1 if a == float('inf') else a for a in node_time])
        