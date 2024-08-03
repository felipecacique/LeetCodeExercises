class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # do a dfs, using every connection just once, try to visit all the nodese twice. 
        # if the noce can by reached though 2 different ways, then ok. If not, it means that there is only one path ot it, and cannot be reached. 
        # if we use the path twice i nthe same direction, lets say [ai, bi] and [ai, bi] as we do a dfs, then there is a cycle that leads to that path. It is not allowed to traverse the path in a reverse order
        
        # if [a,b] is not part of a cycle path, it is a critical connection. Lets find cycles, as we find we return true and add all the conections in post order to an array
        # time/space: O(n)
        from collections import defaultdict
        adj = defaultdict(list)
        for c in connections:
            adj[c[0]].append(c[1])
            adj[c[1]].append(c[0])
        
        seen = set()
        seenConn = set()
        def dfs(node, conn):
            
            # Check if cycle
            if node in seen:
                # when we reach node again, it is the end of the cycle
                cycleHead = set([node])
                return cycleHead

            seen.add(node) 

            cycleHeads = set()
            for neighbour in adj[node]:
                conn = (node, neighbour)
                if conn in seenConn or (conn[1], conn[0])  in seenConn: 
                    continue # don't take the same path twice
                seenConn.add(conn)
                cycleHead = dfs(neighbour, conn)
                if cycleHead: # if we received a non empty set with a cycle head
                    if conn in output: output.remove(conn) # path from cycle, so it is not critical, so lets remove from our output
                    elif (conn[1], conn[0]) in output: output.remove((conn[1], conn[0]))
                    
                    # cycleHeads.update(cycleHead) # add all the cycle heads from its children paths
                    # OBS: The if/else bellow do the same as the commented line above, merging sets. However bellow it is a bit faster
                    if not cycleHeads: 
                        cycleHeads = cycleHead # to make a little bit faster
                    else: 
                        if len(cycleHead) > len(cycleHeads): cycleHead, cycleHeads = cycleHeads, cycleHead
                        cycleHeads.update(cycleHead) # add all the cycle heads from its children paths
                
            if node in cycleHeads:
                # we just found the start of the cycle, so we remove it
                cycleHeads.remove(node)
            
            return cycleHeads

        output = set([ (a,b) for a, b in connections]) 

        dfs(0, [])

        return list(output)



# sabe as above, but above is just cleaner and more optimized
# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         # do a dfs, using every connection just once, try to visit all the nodese twice. 
#         # if the noce can by reached though 2 different ways, then ok. If not, it means that there is only one path ot it, and cannot be reached. 
#         # if we use the path twice i nthe same direction, lets say [ai, bi] and [ai, bi] as we do a dfs, then there is a cycle that leads to that path. It is not allowed to traverse the path in a reverse order
        
#         # if [a,b] is not part of a cycle path, it is a critical connection. Lets find cycles, as we find we return true and add all the conections in post order to an array
#         # time/space: O(n)
#         from collections import defaultdict
#         adj = defaultdict(list)
#         for c in connections:
#             adj[c[0]].append(c[1])
#             adj[c[1]].append(c[0])
        
#         seen = set()
#         pathsFromCycle = set()
#         seenConn = set()
#         def dfs(node, conn, path):
            
#             # Check if cycle
#             if node in seen:
#                 # when we reach node again, it is the end of the cycle
#                 cycleHead = set()
#                 cycleHead.add(node)
#                 return cycleHead

#             seen.add(node) 

#             cycleHeads = set()
#             for neighbour in adj[node]:
#                 conn = [node, neighbour]
#                 if tuple(conn) in seenConn or tuple(conn[::-1]) in seenConn: 
#                     continue # don't take the same path twice
#                 seenConn.add(tuple(conn))
#                 path.append(tuple(conn))
#                 cycleHead = dfs(neighbour, conn, path)
#                 path.pop()
#                 if cycleHead: # if we received a set with a cycle head
#                     pathsFromCycle.add(tuple(conn)) # then this connection is a part of a cycle
#                     cycleHeads = cycleHeads.union(cycleHead) # add all the cycle heads from its children paths
                
                
#             if node in cycleHeads:
#                 # we just found the start of the cycle, so we remove it
#                 cycleHeads.remove(node)
            
#             if cycleHeads:
#                 return cycleHeads
           
#             return None 
            

#         dfs(0, [], [])

#         output = []
#         for a, b in connections:
#             if (a,b) not in pathsFromCycle and (b,a) not in pathsFromCycle:
#                 # [a,b] is not part of a cycle path, so it is a critical connection
#                 output.append([a,b])

#         return output
        