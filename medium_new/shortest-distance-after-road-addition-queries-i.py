class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
        # do a bfs for evey query added to the graph

        from collections import defaultdict
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append(i+1)

        from collections import deque
        def bfs():
            seen = set([0])
            queue = deque()
            queue.append((0,0)) # node, count
            while queue:
                i, count = queue.popleft()
                if i == n-1:    # reached the end
                    return count
                for neighbour in adj[i]:
                    if neighbour not in seen:
                        queue.append((neighbour, count+1))
                        seen.add(neighbour)
        
        output = []
        for u, v in queries:
            adj[u].append(v)    
            count = bfs()
            output.append(count)
        
        return output



# works, but it is slow
# class Solution:
#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#         # use dp
#         output = []
#         queries_ = []
#         for query in queries:
#             queries_.append(query)
#             dp = [n-i-1 for i in range(n)] # contains the distances from ith to the end
#             queries_ = sorted(queries_, reverse=True)
#             for u, v in queries_:
#                 dp[u] = min(dp[u], dp[v] + 1)
#                 for i in range(u-1,-1,-1):
#                     dp[i] = min(dp[i],dp[i+1]+1)
#             output.append(dp[0])
#         return output




# class Solution:
#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#         # use dp
#         output = []
#         q = [(query,i) for i, query in enumerate(queries)]
#         q = sorted(q, reverse=True)
#         for k in range(len(queries)):
#             queries_ = []
#             # get the  k queries
#             for query, idx in q:
#                 if idx <= k: queries_.append(query)
#             dp = [n-i-1 for i in range(n)] # contains the distances from ith to the end
#             for u, v in queries_:
#                 dp[u] = min(dp[u], dp[v] + 1)
#                 for i in range(u-1,-1,-1):
#                     dp[i] = min(dp[i],dp[i+1]+1)
#             output.append(dp[0])
#         return output