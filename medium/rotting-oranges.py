# https://leetcode.com/problems/rotting-oranges/submissions/

# solution similar to the problem number-of-islands


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # do bfs o dfs, propagating a count from the rotten orenges to its children, incrementing 1 fore each children. In case of doing dfs we must use that childre.count = min(new_count, children_count). For bfs we do not need, cus the oranges near to the roten ones will be processed first. And then get the max count. The bfs is faster since we only have to process each orange just once.

             
        from queue import Queue

        m = len(grid)
        n = len(grid[0])

        max_time = 0

        q = Queue()

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 2: # rotten. Let's do a dfs and visit all of the rotten neighbours
                    q.put((i,j,0)) # add the all rotten to the queue
                    grid[i][j] = 0 # mark the node as visited

        # do a breadth-first search
        while not q.empty():
            (i_,j_,time) = q.get()

            max_time = max(max_time, time) # get the max time
            
            if i_+1 < m and grid[i_+1][j_] == 1:  # check if it is a normal orange,  if so we add it to the queue
                grid[i_+1][j_] = 0 # mark the node as visited as soon we add it to he queue, so that each node will be added to the queue only once
                q.put((i_+1, j_, time+1))
            if i_-1 >= 0 and grid[i_-1][j_] == 1: 
                grid[i_-1][j_] = 0 # mark the node as visited
                q.put((i_-1, j_, time+1))
            if j_+1 < n and grid[i_][j_+1] == 1: 
                grid[i_][j_+1] = 0 # mark the node as visited
                q.put((i_, j_+1, time+1))
            if j_-1 >= 0 and grid[i_][j_-1] == 1: 
                grid[i_][j_-1] = 0 # mark the node as visited
                q.put((i_, j_-1, time+1))

        # check if there is a remining orange that  did not get rotten
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1: # we found a good orange
                    return -1

        return max_time
    






# Exactly the same solution as the top one, but using deque() instead of Queue(). deque() is a bit faster.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # do bfs o dfs, propagating a count from the rotten orenges to its children, incrementing 1 fore each children. In case of doing dfs we must use that childre.count = min(new_count, children_count). For bfs we do not need, cus the oranges near to the roten ones will be processed first. And then get the max count. The bfs is faster since we only have to process each orange just once.

             
        from collections import deque

        m = len(grid)
        n = len(grid[0])

        max_time = 0

        q = deque()

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 2: # rotten. Let's do a dfs and visit all of the rotten neighbours
                    q.append((i,j,0)) # add the all rotten to the queue
                    grid[i][j] = 0 # mark the node as visited

        # do a breadth-first search
        while q:
            (i_,j_,time) = q.popleft()

            max_time = max(max_time, time) # get the max time
            
            if i_+1 < m and grid[i_+1][j_] == 1:  # check if it is a normal orange,  if so we add it to the queue
                grid[i_+1][j_] = 0 # mark the node as visited as soon we add it to he queue, so that each node will be added to the queue only once
                q.append((i_+1, j_, time+1))
            if i_-1 >= 0 and grid[i_-1][j_] == 1: 
                grid[i_-1][j_] = 0 # mark the node as visited
                q.append((i_-1, j_, time+1))
            if j_+1 < n and grid[i_][j_+1] == 1: 
                grid[i_][j_+1] = 0 # mark the node as visited
                q.append((i_, j_+1, time+1))
            if j_-1 >= 0 and grid[i_][j_-1] == 1: 
                grid[i_][j_-1] = 0 # mark the node as visited
                q.append((i_, j_-1, time+1))

        # check if there is a remining orange that  did not get rotten
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1: # we found a good orange
                    return -1

        return max_time