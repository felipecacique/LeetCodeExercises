class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/flower-planting-with-no-adjacent/
        # inspired in https://www.youtube.com/watch?v=-jsO_KK2HaI

        # Create the adj list
        adj = {}
        for x, y in paths:
            adj[x] = adj.get(x,[]) + [y]
            adj[y] = adj.get(y,[]) + [x]

        gardenColors = [0] * n
        for i in range(1, n+1):
            colors = [True] * 5 # ignore the position 0, and we have left the 4 colours, indicating if that color is available for the ith garden
            # Check the neighbours and find out what colors were not used yet
            if i in adj:
                for neighbour in adj[i]:
                    # gardenColors[neighbour] return the color of the neighbour. It returns 0 if there is no color
                    colors[gardenColors[neighbour-1]] = False # here we acess the index of the neightbour color and remove it from colors
            for j in range(1, 5):
                if colors[j] == True: 
                    gardenColors[i-1] = j
                    break
        return gardenColors