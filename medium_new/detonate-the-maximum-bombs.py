class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # https://leetcode.com/problems/detonate-the-maximum-bombs/
        # O(n^2) to create the graph (adj list) and O(n^2) to traverse the graph starting from every node
        
        # Create graph
        adj = [[] for _ in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                distance = (bombs[j][0] - bombs[i][0])**2 + (bombs[j][1] - bombs[i][1])**2
                if distance <= bombs[i][2]**2: adj[i].append(j)
                if distance <= bombs[j][2]**2: adj[j].append(i)

        # Traverse graph from every node
        def detonate(i):
            exploded.add(i)
            count = 0
            for j in adj[i]:
                if not j in exploded:
                    count += detonate(j)
            return count + 1

        maxBombs = 0
        for i in range(len(bombs)):
            exploded = set()
            count = detonate(i)
            maxBombs = max(count, maxBombs)

        return maxBombs