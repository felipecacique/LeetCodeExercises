class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        grid.append([float('inf')]*len(grid[0]))
        for i in range(len(grid)):
            grid[i].append(float('inf'))

        for i in range(len(grid)-2, -1, -1):
            for j in range(len(grid[i])-2, -1, -1):
                if (i == len(grid)-2 and j == len(grid[i])-2):
                    continue
                grid[i][j] += min(grid[i][j+1], grid[i+1][j])
        
        return grid[0][0]
