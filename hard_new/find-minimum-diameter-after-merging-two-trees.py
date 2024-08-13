class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
        # connect them at the middle point of both trees. Find the max path, all its nodes, and get the middle
        # try an approach similar to the exercise of finding the longest path ; we dont need to have a list with all nodes, only the size
        # O(n)

        from collections import defaultdict
        adj1 = defaultdict(list)
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)
        
        adj2 = defaultdict(list)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)


        def getLongestPath(node):
            if adj[node] == []: # leaf
                return 1

            paths = []
            for neighbour in adj[node]:
                if not neighbour in seen:
                    seen.add(neighbour)
                    path = getLongestPath(neighbour)
                    paths.append(path)

            if paths == []: return 1 # leaf

            # chose the longest path ( it is a path that goes from a child )
            paths = sorted(paths, reverse=True) # this part can be optimized to remove the sort function
            max_path = paths[0]
            second_max_path = paths[1] if len(paths) >= 2 else None
             
            # return the max path from _>   child branch -> node -> child branch
            # and also return the math path inchuding node, that will be used by the parent node
            if second_max_path != None: 
                possibleMaxPath = max_path + 1 + second_max_path
                if possibleMaxPath > longestPath[0]:
                    longestPath[0] = possibleMaxPath
            
            possibleMaxPath2 = max_path + 1
            if possibleMaxPath2 > longestPath[0]:
                longestPath[0] = possibleMaxPath2
            
            return max_path + 1

        # Get the max path of the first tree
        adj = adj1
        seen = set([0])
        longestPath = [0] # path
        getLongestPath(0)
        longestPath1 = longestPath[0]

        # Get the max path of the second tree
        adj = adj2
        seen = set([0])
        longestPath = [0] # path
        getLongestPath(0)
        longestPath2 = longestPath[0]

        # Calculate the radius based on the longest path of the trees, imagining that we link them by the middle node.
        sol = 1
        sol = max(sol,longestPath1-1, longestPath2-1)  
        s1 = max(longestPath1//2+1, longestPath1 - longestPath1//2)
        s2 = max(longestPath2//2+1, longestPath2 - longestPath2//2)
        sol = max(sol, s1+s2-1)

        return sol
    



# class Solution:
#     def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
#         # connect them at the middle point of both trees. Find the max path, all its nodes, and get the middle
#         # try an approach similar to the exercise of finding the longest path
#         # O(n)

#         from collections import defaultdict
#         adj1 = defaultdict(list)
#         for a, b in edges1:
#             adj1[a].append(b)
#             adj1[b].append(a)
        
#         adj2 = defaultdict(list)
#         for u, v in edges2:
#             adj2[u].append(v)
#             adj2[v].append(u)


#         def getLongestPath(node):
#             if adj[node] == []: # leaf
#                 return [node]

#             paths = []
#             for neighbour in adj[node]:
#                 if not neighbour in seen:
#                     seen.add(neighbour)
#                     path = getLongestPath(neighbour)
#                     paths.append((len(path), path))

#             if paths == []: return [node] # leaf

#             # chose the longest path ( it is a path that goes from a child )
#             paths = sorted(paths, reverse=True) # this part can be optimized to remove the sort function
#             max_path = paths[0]
#             second_max_path = paths[1] if len(paths) >= 2 else None
             
#             # return the max path from _>   child branch -> node -> child branch
#             # and also return the math path inchuding node, that will be used by the parent node
#             if second_max_path != None: 
#                 possibleMaxPath = max_path[1] + [node] + list(reversed(second_max_path[1]))
#                 if len(possibleMaxPath) > len(longestPath[0]):
#                     longestPath[0] = possibleMaxPath
            
#             possibleMaxPath2 = max_path[1] + [node]
#             if len(possibleMaxPath2) > len(longestPath[0]):
#                 longestPath[0] = possibleMaxPath2
            
#             return max_path[1] + [node]

#         adj = adj1
#         seen = set([0])
#         longestPath = [[]] # path
#         getLongestPath(0)
#         longestPath1 = longestPath[0]
#         # node1 = longestPath[0][len(longestPath[0])//2]
#         # print(longestPath1)

#         adj = adj2
#         seen = set([0])
#         longestPath = [[]] # path
#         getLongestPath(0)
#         longestPath2 = longestPath[0]
#         # node2 = longestPath[0][len(longestPath[0])//2]
#         # print(longestPath2)

#         # longestPath1 = [-1] + [ a for a in longestPath1 ] + [-1]
#         # longestPath2 = [-1] + [ a for a in longestPath2 ] + [-1]
#         # print(longestPath1)


#         sol = 1
#         sol = max(sol,len(longestPath1)-1, len(longestPath2)-1)  
#         # sol = max(sol,len(longestPath1)-1-2, len(longestPath2)-1-2)  
#         s1 = max(len(longestPath1)//2+1, len(longestPath1) - len(longestPath1)//2)
#         s2 = max(len(longestPath2)//2+1, len(longestPath2) - len(longestPath2)//2)

#         # sol = max(sol, s1+s2+1-2)
#         sol = max(sol, s1+s2-1)

#         return sol