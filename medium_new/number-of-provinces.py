class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75
        # start from node i and visit all of its neightbour, and remove them from the matrix.After wi finhish, we count this as a province, and get a node that has not been yet visited.
        def Solution1():
            provinces = 0

            visited = set()
            from collections import deque
            queue = deque()

            n = len(isConnected)
            
            for i in range(0,n): # start from every single node not yet seen
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

                    while queue: # visiting all path nodes reachable from i node
                        node = queue.popleft()
                        for j in range(0,n):
                            if isConnected[node][j] and j not in visited:
                                queue.append(j)
                                visited.add(j) # mark as already visited
                    
                    provinces += 1

            return provinces

        def Solution2(): # using recursion and dfs instead of queue
            
            def dfs(city):
                visited.add(city)
                for neighbor in range(len(isConnected)):
                    if isConnected[city][neighbor] == 1 and neighbor not in visited:
                        dfs(neighbor)

            provinces = 0
            visited = set()
            for city in range(0,len(isConnected)): # start from every single node not yet seen
                if city not in visited:
                    dfs(city)
                    provinces += 1

            return provinces


        return Solution1()
                            