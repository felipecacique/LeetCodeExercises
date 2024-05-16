class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # https://leetcode.com/problems/find-the-safest-path-in-a-grid/?envType=daily-question&envId=2024-05-15
        # O(n^2)

        # --> Part1: do the dp by filling the grid with the min distance to a thief. 
        
        n = len(grid)

        from collections import deque

        queue = deque()
        seen = set()
        
        # add all 1s
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r,c,0))
                grid[r][c] = -1
        
        # fill the grid with the factor, expanding from 1's
        while queue:
            r, c, factor = queue.popleft()
            
            if grid[r][c] == -1:
                grid[r][c] = factor
            
            if r+1 < n and (r+1,c) not in seen: 
                queue.append((r+1,c,factor+1))
                seen.add((r+1,c))
            if r-1 >= 0 and (r-1,c) not in seen: 
                queue.append((r-1,c,factor+1))
                seen.add((r-1,c))
            if c+1 < n and (r,c+1) not in seen: 
                queue.append((r,c+1,factor+1))
                seen.add((r,c+1))
            if c-1 >= 0 and (r,c-1) not in seen: 
                queue.append((r,c-1,factor+1))
                seen.add((r,c-1))

        # --> Part2: Then do the bfs prioratizing the paths with maximum safesness factor found so far. No need to campute all the paths, since we only need the max fator. We can use a priority queue (heap). Since we will never visit the same cell twice, we have time complexity O(n^2) by visiting every cell once      

        import heapq

        max_factor = 0
        heap = [(-grid[0][0], 0, 0)]
        heapq.heapify(heap)
        seen = set()

        # expands the paths prioritizing the path with the maximum safeness factor
        while heap:
            minimum_dist, r, c = heapq.heappop(heap)
            minimum_dist = -minimum_dist
            
            if r == n-1 and c == n-1: # path reached the end
                return minimum_dist

            if r+1 < n and (r+1,c) not in seen: 
                heapq.heappush(heap, (-min(minimum_dist,grid[r+1][c]), r+1, c))
                seen.add((r+1,c))
            if r-1 >= 0 and (r-1,c) not in seen: 
                heapq.heappush(heap, (-min(minimum_dist,grid[r-1][c]), r-1, c))
                seen.add((r-1,c))
            if c+1 < n and (r,c+1) not in seen: 
                heapq.heappush(heap, (-min(minimum_dist,grid[r][c+1]), r, c+1))
                seen.add((r,c+1))
            if c-1 >= 0 and (r,c-1) not in seen: 
                heapq.heappush(heap, (-min(minimum_dist,grid[r][c-1]), r, c-1))
                seen.add((r,c-1))

        return 0