# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def Solution1(grid):
            # do a bfs through the 1s, removing visited nodes from the graph. If connected 1s has ended, islands += 1 and we get the next node, until we find 1. Do a bfs and repeat the whole process untill we have visited all nodes.
            from queue import Queue
            q = Queue()

            m = len(grid)
            n = len(grid[0])

            islands = 0

            for i in range(0,m):
                for j in range(0,n):

                    if grid[i][j] == '1': # land. Let's do a bfs and visit all of the island land
                        islands += 1
                        q = Queue()
                        q.put((i,j))

                        while not q.empty():
                            (i_,j_) = q.get()
                            if grid[i_][j_] == '1': # if it is a land, we keep exploring this node, otherwise not cus we have found water
                                
                                grid[i_][j_] = 0 # mark the node as visited
                                if i_+1 < m: q.put((i_+1, j_))
                                if i_-1 >= 0: q.put((i_-1, j_))
                                if j_+1 < n: q.put((i_, j_+1))
                                if j_-1 >= 0: q.put((i_, j_-1))

            return islands
        
        def Solution2(grid): # same as Solution1 but a bit optimized
        
            from queue import Queue

            m = len(grid)
            n = len(grid[0])

            islands = 0

            for i in range(0,m):
                for j in range(0,n):

                    if grid[i][j] == '1': # land. Let's do a bfs and visit all of the island land
                        islands += 1
                        q = Queue()
                        q.put((i,j))
                        grid[i][j] = '0' # mark the node as visited

                        while not q.empty():
                            # print(q.qsize())
                            (i_,j_) = q.get()
                            
                            if i_+1 < m and grid[i_+1][j_] == '1': 
                                grid[i_+1][j_] = '0' # mark the node as visited as soon we add it to he queue, so that each node will be added to the queue only once. It my be quicker
                                q.put((i_+1, j_))
                            if i_-1 >= 0 and grid[i_-1][j_] == '1': 
                                grid[i_-1][j_] = '0' # mark the node as visited
                                q.put((i_-1, j_))
                            if j_+1 < n and grid[i_][j_+1] == '1': 
                                grid[i_][j_+1] = '0' # mark the node as visited
                                q.put((i_, j_+1))
                            if j_-1 >= 0 and grid[i_][j_-1] == '1': 
                                grid[i_][j_-1] = '0' # mark the node as visited
                                q.put((i_, j_-1))

            return islands


        def Solution3(grid): # Fastest Solution!! same as Solution2 but using dfs intead of bfs. Its seems that using the bult-in list operations in python is faster than using a queue library with comand of pop() and get()

            m = len(grid)
            n = len(grid[0])

            islands = 0

            for i in range(0,m):
                for j in range(0,n):

                    if grid[i][j] == '1': # land. Let's do a bfs and visit all of the island land
                        islands += 1
                        q = []
                        q.append((i,j))
                        grid[i][j] = '0' # mark the node as visited

                        while q:
    
                            (i_,j_) = q.pop()
                            
                            if i_+1 < m and grid[i_+1][j_] == '1': 
                                grid[i_+1][j_] = '0' # mark the node as visited as soon we add it to he queue, so that each node will be added to the queue only once. It my be quicker
                                q.append((i_+1, j_))
                            if i_-1 >= 0 and grid[i_-1][j_] == '1': 
                                grid[i_-1][j_] = '0' # mark the node as visited
                                q.append((i_-1, j_))
                            if j_+1 < n and grid[i_][j_+1] == '1': 
                                grid[i_][j_+1] = '0' # mark the node as visited
                                q.append((i_, j_+1))
                            if j_-1 >= 0 and grid[i_][j_-1] == '1': 
                                grid[i_][j_-1] = '0' # mark the node as visited
                                q.append((i_, j_-1))

            return islands

        return Solution3(grid)



