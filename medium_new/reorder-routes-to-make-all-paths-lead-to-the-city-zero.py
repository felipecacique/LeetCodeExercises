class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/submissions/1351503786/
        # O(n)
        from collections import defaultdict
        adj = defaultdict(list)
        adjRev = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adjRev[b].append(a)
        
        count = 0
        queue = [0]
        seen = set([0])
        while queue:
            i = queue.pop()
            
            if i in adj:
                for j in adj[i]: # connections that are leavning i
                    if j in seen: continue
                    seen.add(j)
                    queue.append(j)
                    count += 1 # we count 1, because we found a connection that is leaving i, instead of reaching i
                
            if i in adjRev: # conncections that are reaching i
                for j in adjRev[i]:
                    if j in seen: continue
                    seen.add(j)
                    queue.append(j)

        return count
        