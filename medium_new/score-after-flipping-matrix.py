class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # https://leetcode.com/problems/score-after-flipping-matrix/description/?envType=daily-question&envId=2024-05-13
        # the move order does not matter. A matrix mxn a has m*n possible moves. O(M*N*m)
        # lets try a greedy algorithm inverting the smallest numbers first. row first, making evry line becoming the biggest number it can be with line modes. then e do the columns. If the move in the column leads to a new numbers, and those new num sum is gretter than the prev numbers, then we do the move.
        # O(M*N)

        m = len(grid)
        n = len(grid[0])
        largestNum = pow(2,n)-1

        # do first the row moves
        for j in range(m):
            num = int("".join([str(a) for a in grid[j]]), 2)
            complement = largestNum - num 
            if complement > num: # if inverting the row leads to a largest number, then we invert it
                # do the row move
                for i in range(n):
                    # grid[j][i] = (0 if grid[j][i] == 1 else 1) # invert bit
                    grid[j][i] = 1 - grid[j][i] # invert bit
        
        # do the column moves (micro adjustments)
        for col in range(n):
            columnSum = 0
            for row in range(m):
                columnSum += grid[row][col]
            complement = m - columnSum
            if complement > columnSum:
                # invert the column since it leads to a greatter sum
                for row in range(m):
                    # grid[row][col] = (0 if grid[row][col] == 1 else 1) # invert 1
                    grid[row][col] = 1 - grid[row][col]
     
        # compute the answer by summing all num
        ans = 0
        for j in range(m):
            ans += int("".join([str(a) for a in grid[j]]), 2)

        return ans