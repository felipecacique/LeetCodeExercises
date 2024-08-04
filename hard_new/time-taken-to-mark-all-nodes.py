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

            if not node in adj:
                solutionFromButtom[node] = 0
                return 0

            for neighbour in adj[node]:
                solButtom = getSolutionFromButtom(neighbour)
                solButtom = solButtom + 2 if neighbour % 2 == 0 else solButtom + 1
                solutionFromButtomDict[(node, neighbour)] = solButtom
                solutionFromButtom[node] = max(solutionFromButtom[node], solButtom)
            
            return solutionFromButtom[node]


        import heapq
        
        def getSolutionFromTop(node, solTop):
            
            if not node in adj:
                solutionFromTop[node] = solTop
                solution[node] = solutionFromTop[node]
                return

            # get the max and the second max from neighbours
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
                if solNeighbour != maxSolutionFromButtom: solNode = max(solNode, maxSolutionFromButtom)
                else: solNode = max(solNode, maxSolutionFromButtom2)
                solutionFromTop[node] = solNode
                solution[node] = max(solutionFromTop[node], solutionFromButtom[node])

                getSolutionFromTop(neighbour, solNode + 2 if node % 2 == 0 else solNode + 1)


        getSolutionFromButtom(0)
        getSolutionFromTop(0, 0)

        return solution