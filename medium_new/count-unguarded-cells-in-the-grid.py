class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2024-11-21
        # O(M*N)
        grid = [ [0] * n for _ in range(m) ]
        for row, col in guards:
            grid[row][col] = "G"
        for row, col in walls:
            grid[row][col] = "W"

        for row, col in guards:
            for r in range(row+1,m):
                if grid[r][col] in [0,1]: grid[r][col] = 1
                else: break
            for r in range(row-1,-1,-1):
                if grid[r][col] in [0,1]: grid[r][col] = 1
                else: break
            for c in range(col+1,n):
                if grid[row][c] in [0,1]: grid[row][c] = 1
                else: break
            for c in range(col-1,-1,-1):
                if grid[row][c] in [0,1]: grid[row][c] = 1
                else: break
        
        count = 0
        for col in range(n):
            for row in range(m):
                 if grid[row][col] == 0: count += 1
        
        return count
             