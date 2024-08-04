class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
        # because of the restriction, we can solve it more efficiently with intervals
        # based on this solution here https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/solutions/5584116/best-python-solution-beats-100-in-terms-of-time-and-space/
        # tima and space O(n)

        output = []
        adj = {}
        for i in range(n-1):
            adj[i]=i+1
        
        for u, v in queries:
            # if the query interval is inside another interval, then no need to do anything
            if u not in adj or v<=adj[u]:
                output.append(len(adj))
                continue
            
            # remove all nodes between query interval, following the graph. This way we can avoind traying to remove the same nodes twice. Since each node will be removed just once, out time complexity is O(n) 
            node = adj[u] # we will start from the node that u points to
            while node < v: 
                aux = adj[node]
                del adj[node] # remove all paths between [u,v]
                node = aux
            adj[u]=v # now we can add the query interval
            output.append(len(adj))
        return output

# still slow since we try to remove the same removed nodes over and over again. It threse were a way to junp the already popped nodes ... see solution above

# class Solution:
#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#         # https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
#         # because of the restriction, we can solve it more efficiently 
#         # O(n + Q*n)

#         output = []
#         s = set()
#         for i in range(n):
#             s.add(i)
#         for u, v in queries:
            
#             if u not in s or v not in s: # little optimization
#                 output.append(len(s)-1)
#                 continue

#             for x in range(u+1, v):
#                 if x in s: s.remove(x)
#                 # else: break
            
#             # for x in range(v-1, u, -1):
#             #     if x in s: s.remove(x)
#             #     else: break

#             output.append(len(s)-1)
#         return output



# works but still slow
# class Solution:
#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#         # https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
#         # because of the restriction, we can solve it more efficiently with intervals

#         output = []
#         intervals = [(float('inf'), float('inf'))]
#         for query in queries:# add queries one by one
#             # print(query)
#             newIntervals = []
#             added = False
#             jump = 0 # the number of nodes that the intervals allow us to jump
#             # add query to the interval list
#             for interval in intervals:
#                 if interval[0] <= query[0] and interval[1] >= query[1]: # query is inside an interval, so we must not add the query to the intervals list
#                     added = True
#                 elif query[1] <= interval[1] and not added:
#                     newIntervals.append(query)
#                     jump += query[1] - query[0] - 1
#                     added = True
#                 if not(interval[0] >= query[0] and interval[1] <= query[1]): # the interval is inside the query interval, so we will only keep the query interval
#                     newIntervals.append(interval)
#                     jump += interval[1] - interval[0] - 1 if interval[0] != float("inf") else 0
                
#             intervals = newIntervals
#             output.append(n-jump-1)
#             # print(intervals)
#         return output


# class Solution:
#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#         # https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
#         # do a bfs for evey query added to the graph
#         # O(query.len * (edges+nodes))

#         from collections import defaultdict
#         adj = defaultdict(list)
#         for i in range(n-1):
#             adj[i].append(i+1)

#         from collections import deque
#         def bfs():
#             seen = set([0])
#             queue = deque()
#             queue.append((0,0)) # node, count
#             while queue:
#                 i, count = queue.popleft()
#                 if i == n-1:    # reached the end
#                     return count
#                 for neighbour in adj[i]:
#                     if neighbour not in seen:
#                         queue.append((neighbour, count+1))
#                         seen.add(neighbour)
        
#         output = []
#         for u, v in queries:
#             adj_u = adj[u].pop()
#             adj[u].append(max(adj_u, v))    
#             count = bfs()
#             output.append(count)
        
#         return output