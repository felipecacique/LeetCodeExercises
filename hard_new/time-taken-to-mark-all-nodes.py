class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/time-taken-to-mark-all-nodes/
        # very dificult implementation. I saw the hints before solving it. Inspired the in the exercise of finding the longest path in a tree
        # calculate the solution from the bottom (dp), and the traverse againg top down genereating the solutions from the top
        
        n = 0
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            if u < v: adj[u].append(v)
            else: adj[v].append(u)
            n = max(n, u+1, v+1)
     
        solution = [0] * n
        solutionFromButtomDict = {}
        solutionFromButtom = [0] * n
        solutionFromTop = [0] * n

        def getSolutionFromButtom(node):
            # Get the solution from the bottom children, post order traversal, (button up approach), using dp. The solution of node sol(node) = mox(sol(children), ...). And we have to add something to each sol(children) that is 1 if children is odd and 2 if it is even.

            if not node in adj:
                solutionFromButtom[node] = 0
                return 0

            for neighbour in adj[node]:
                solButtom = getSolutionFromButtom(neighbour)
                solButtom = solButtom + 2 if neighbour % 2 == 0 else solButtom + 1 # apply the rule. So the solution toist node from the path neighbour1, is the solution of neighbour1 plus 1 or 2, deppending is neighbour1 is odd or even
                solutionFromButtomDict[(node, neighbour)] = solButtom
                solutionFromButtom[node] = max(solutionFromButtom[node], solButtom)
            
            return solutionFromButtom[node]


        import heapq

        def getSolutionFromTop(node, solTop):
            # Top down approach, pre order traversal. Each node receives the solution from the parent node, and we also have the solution from every children node (from the bottom) gotten previosly.
            # so the solution of the node, is the max between the solution of the parent and the soluion of every children paths.
            # the node must send its solution to the children ith (solNode) added 1 or 2 deppending if node is even or odd. But this solution solNode we will send to the children ith must have excluded in its calculation the path from ith.  
            
            if not node in adj:
                solutionFromTop[node] = solTop
                solution[node] = solutionFromTop[node]
                return

            #this chunck of code gets the max and the second max from neighbours. This is just to make it more time efficient when excluding the neighbour path from solNode
            solNeighbours = []
            for neighbour in adj[node]:
                solNeighbour = solutionFromButtomDict[(node, neighbour)] 
                solNeighbours.append(-solNeighbour)
            heapq.heapify(solNeighbours)
            maxSolutionFromButtom = 0
            maxSolutionFromButtom2 = 0
            if solNeighbours: maxSolutionFromButtom = - heapq.heappop(solNeighbours)
            if solNeighbours: maxSolutionFromButtom2 = - heapq.heappop(solNeighbours)

            for neighbour in adj[node]:
                solNode = solTop
                solNeighbour = solutionFromButtomDict[(node, neighbour)]
                # Exclude the neighbout node from the max calculation. Instead of doing a new for and doing the max of all neighbours except neighbour ith, we can just do as follow. No need for and extre loop.
                if solNeighbour != maxSolutionFromButtom: solNode = max(solNode, maxSolutionFromButtom)
                else: solNode = max(solNode, maxSolutionFromButtom2)
                
                solutionFromTop[node] = solNode
                solution[node] = max(solutionFromTop[node], solutionFromButtom[node]) # get the max time from every edge, from the bottoms and from the tops

                getSolutionFromTop(neighbour, solNode + 2 if node % 2 == 0 else solNode + 1)


        getSolutionFromButtom(0)
        getSolutionFromTop(0, 0)

        return solution