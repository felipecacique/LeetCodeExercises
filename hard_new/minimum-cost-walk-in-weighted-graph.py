class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
        
        from collections import defaultdict
        adj = defaultdict(list)
        weights = {}
        minPossible = 2**31-1
        for u, v, w in edges:
            adj[u].append(v)
            adj[v].append(u)
            weights[(u,v)] = w if (u,v) not in weights else weights[(u,v)] & w # handle the multiple edges from u to v
            weights[(v,u)] = w if (v,u) not in weights else weights[(v,u)] & w
            minPossible &= w


        from collections import deque
        def bfs(s,t):
            # if we there is a path from s to t, the solution is equal to an & of all edges of the connected graph. If the cost was the sum of the weights, we would have to implement a dijkstra with heap
            queue = deque([s])
            seen = set()
            minPathCost = 2**31-1
            reachedT = False
            while queue: # do a bfs
                u = queue.popleft()
                if u == t: reachedT = True
                if minPathCost <= minPossible and reachedT: break
                for v in adj[u]:
                    if (u,v) not in seen:
                        minPathCost = minPathCost & weights[(u,v)]
                        queue.append(v)
                        seen.add((u,v))
            
            return minPathCost if reachedT else -1

        answer = []    
        for s, t in query:
            pathCost = bfs(s,t)
            answer.append(pathCost)
        
        return answer




# works but too slow
# class Solution:
#     def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
#         from collections import defaultdict
#         adj = defaultdict(list)
#         weights = {}
#         minPossible = 2**31-1
#         for u, v, w in edges:
#             adj[u].append(v)
#             adj[v].append(u)
#             weights[(u,v)] = w if (u,v) not in weights else weights[(u,v)] & w
#             weights[(v,u)] = w if (v,u) not in weights else weights[(v,u)] & w
#             minPossible &= w

#         # print(adj, weights)
#         import heapq
#         from collections import deque
#         def dijkstra(s,t):
#             heap = [(2**31-1,s)] 
#             queue = deque([(2**31-1,s)])
#             seen = set()
#             minPathCost = float('inf')
#             minPathSeen = {}
#             while heap: # do a bfs but prioritizing the paths with smaller costs first
#                 # print(heap)
#                 pathCost, u = heapq.heappop(heap)
#                 # pathCost, u = queue.popleft()
#                 # print(pathCost, u)
#                 if u == t:
#                     # reached my destination
#                     # return pathCost
#                     minPathCost = min(minPathCost, pathCost)
#                     if minPathCost <= minPossible: break

#                 for v in adj[u]:
#                     # if (u,v) not in seen:
#                     # if pathCost == 2**31-1: newPathCost = weights[(u,v)]
#                     newPathCost = pathCost & weights[(u,v)]
#                     # if newPathCost < pathCost:
#                     # if (u,v,newPathCost) not in seen:
#                     if (u,v) not in minPathSeen or newPathCost < minPathSeen[(u,v)]:
#                         heapq.heappush(heap,(newPathCost,v))
#                         # queue.append((newPathCost,v))
#                         # seen.add((u,v,newPathCost))
#                         minPathSeen[(u,v)] = newPathCost
            
#             return minPathCost if minPathCost != float('inf') else -1

#         answer = []    
#         for s, t in query:
#             pathCost = dijkstra(s,t)
#             answer.append(pathCost)
        
#         return answer


