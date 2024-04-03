class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # bfs starting from rotten oranges
        m = len(grid)
        n = len(grid[0])
        
        from collections import deque
        queue = deque()
        seen = set()
        
        total_oranges = 0
        total_rotten = 0
        max_minutes = 0
        # put all rotten in the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append( (i,j,0) )
                    seen.add( (i,j) )
                if grid[i][j] != 0:
                    total_oranges += 1
                    
        # do the bfs. when oranges stops to turn rotten in a given intereaction, then we stop 
        while queue:      
            i, j, minutes = queue.popleft()
            total_rotten += 1
            max_minutes = max(max_minutes, minutes)

            if (i, j+1) not in seen and j+1 < n and grid[i][j+1] == 1: # becomes rotten
                queue.append( (i, j+1, minutes+1) )
                seen.add( (i, j+1) ) 
                
            if (i, j-1) not in seen and j-1 >= 0 and grid[i][j-1] == 1: # becomes rotten
                queue.append( (i, j-1, minutes+1) )
                seen.add( (i, j-1) )   
                
            if (i+1, j) not in seen and i+1 < m and grid[i+1][j] == 1: # becomes rotten
                queue.append( (i+1, j, minutes+1) )
                seen.add( (i+1, j) )   
                
            if (i-1, j) not in seen and i-1 >= 0 and grid[i-1][j] == 1: # becomes rotten
                queue.append( (i-1, j, minutes+1) )
                seen.add( (i-1, j) )   
        
        if total_rotten >= total_oranges:
            return max_minutes
        else:
            return -1