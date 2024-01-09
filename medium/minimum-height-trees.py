# https://leetcode.com/problems/minimum-height-trees/submissions/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # GO TO SOLUTION 4!! 

        # lets compute the max distance from a node. That is for the node i, store in it the size of the max path from it. Example: in the Example 2, the node i=3 has the max distance of 2, which is the path 3 -> 4 -> 5. the Then get the node with minimum max distance among all. This is the root of our MHT. The question here now is how to calculate the max distance in all nodes at once, in a single iteration? dijkstra inspiration? Notice that the max distance of a node i is the max between its neighbours/children values + 1. Solution 1 - One solution is doing k iteractions, where k is the max distance ever calculated. We start every node with 0, and at every iteraction its sums incrase by 1. It is like a propagation. At every iteraction we are propagating the distances, like "heat", until there is no change in the distance. This is the point where we stop the algorithm. Complexity of this is time O(n*k). Solution 2: Can we find a topological order in which we do the solution 1 approach but with only one iteraction? start from the leafs, that are nodes with only one connection, and then goes to theyr parents nodes and so on. We will visit all the nodes, and keep visiting and updatind the distances untill there is no distances left to update. We start from the leaf nodes untill we reach the leaf nodes again. If we reah a leaf a leaf, we do not propagate from there. The "pulse" signal start from the leafs and end in the leafs.

        # solution 3 - what if instead of unsing the max distance, we use the min distance. To calculate the min distance we can start from the leaf nodes (nodes with only one conection), since their min distance is 0, then move to their connections, and so on. The we would get the the nodes with the higher min distance.  No, this might not work ..

        # SOLUTION 4!! - imagine a rope with length d. The middle point is right in the middle the rope, r=d/2. The both sides will have the same lenght. One way to find the middle of a rope is setting fire to the both ends at the same time. The fire moves at the same speed and where the fire meets, that is the middle. We will do the same thing here. Imagine the tree as a rope, where there is the largest distance from side to side (lets call the diameter). The vertice that divide it in 2 pieces of same length is right in the middle of it, such like the rope analogy. We will start from the leaves (vertices that has only one edge), through a bfs, we will visit all the nodes (as we visit them it is like a rope getting fire from the ends to the middle). The last node(s) to be visited is the middle of the MHTs, since it divides the diameter in 2 equal parts. But note that there might be more than one MHT root node. So as we visit them we will keep track of the count, and will update its count (or distance) to the longest leaf while we do the bfs. Each node will hold the max distance (or max count) that have reach it so far. Well, this is the information of the max path to it, which is the path corresponding to the "diameter". The smaler paths does not influence anything, so we just ignore them and compute the max. Each vertice will be traveled only once, and we finish the bfs after all node has been processed (it happens when there is only one edge left to process. It has got the signal from the others edges, and now it will use the only edge left to propagate the signal). Finally we get the nodes in which the count is max. That is our answer. Time O(n+m), linear. Such a tough question to do and explain hehe. I think we can solve this problem withough having to compute the count, only by getting the last node to be processed, when the last two "pointers" meet.

        def Solution4(n, edges):
            
            max_distance = [0] * n # the list holds the max distance of each node in ith

            connections = [0] * n # get the number of connection of that node. Nodes with one connections are leaves
            for edge in edges:
                a, b = edge
                connections[a] += 1
                connections[b] += 1
            
            # create an adjacent list
            adj = [[] for _ in range(0,n)] # list of lists where ith represents the node, and adj[i] holds the i connected nodes
            for edge in edges:
                a, b = edge
                adj[a].append(b) # a is connected to b
                adj[b].append(a) # b is connected to a

            seen = set()

            # lets do a bfs
            from collections import deque
            queue = deque()

            # add all the leaf nodes first
            for i, c in enumerate(connections):
                if c == 1: # leaf
                    queue.append( (i, 0) ) 
            
            while len(queue) > 0:
                
                node, dist = queue.popleft()

                if not node in seen: # we only can visit a fully processed node once
                    
                    # process the node
                    max_distance[node] =  max(dist+1, max_distance[node]) # stores the max distance to this node so far
                    connections[node] -= 1  # we have just processed one connection. This list will hold the number of connections left to process

                    # check if node is fully processed. It will happend when there is only one edge left to process. So we must not come back to this node ever. It has got the signal from the others, and now it will use the only edge left to propagate the signal
                    if connections[node] <= 1: 
                        seen.add(node)
                        for n in adj[node]: # add its connections to the queue
                            queue.append( (n, max_distance[node]) ) # we will add the node's connections to the queue and the node's max_distance
                    

            # get the indexes to the max value in max_distance array
            index_max = []
            max_d = max(max_distance)
            for i, d in enumerate(max_distance):
                if d == max_d:
                    index_max.append(i)

            return index_max

        return Solution4(n, edges)










