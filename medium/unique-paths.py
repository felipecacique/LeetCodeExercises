# https://leetcode.com/problems/unique-paths/submissions/

class Solution:
    
    # both solutions are equally fast and great

    def uniquePaths(self, m: int, n: int) -> int:
        
        def Solution1(m,n):
            # using math only. time O(1) or O(m*n) depending on the time complexity of the factorial operation, which I do not know

            # a = m-1
            # b = n-1
            # total = a+b

            # # total! / (a! * b!)
            
            # import math

            # return int(math.factorial(total)/(math.factorial(a)*math.factorial(b)))

            from math import factorial

            return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
        

        def Solution2(m,n):
            # using dinamic programing. Solution from https://www.youtube.com/watch?v=IlEsdxuD4lY&ab_channel=NeetCode. We start from the goal point, and will fill each cell with the number of possibilities to get to the goal from thta specific position. And this can be made iteratively, using the already calculated solutions form the left and down cells. Lets dice into it. The last row can be filled all with 1, if the robot is in any of that cell, the only way to go to the finish goal is moving right only, since it has already went all the way down. The same is valif for the last column. Now lets get the closest diagonal cell to goal. The are 2 possible actions from there: left and down. If we go left, we reach a cell in the last column, that is filled with 1 (one way to the goal). If we go down, we reach a cell in the last row, that is also filled with 1. Then, from this diagonal, we have 2 possibilities (left and right), and each one leads to 1 path. So we fill the diagonal with 2 (1 from right + 1 from down). The cell on the left of the diagonal, can move right and down. If it move right, it reach the number 2. If it go down, it reach 1. So there is 3 possibilities from that cell (2 + 1). We repeat this process untill all cell is filled in, and return the value that is on start. Time O(m*n)


            grid = [[1] * n  for _ in range(0, m)]

            # for i in range(0, n):
            #     grid[-1][i] = 1 # fill last row with ones
            
            # for j in range(0, m):
            #     grid[j][-1] = 1 # fill last column with ones
            
            # lets calculate the rows first, from bottom to top, right to left
            for j in range(m-2, -1, -1): # right to left
                for i in range(n-2, -1, -1): # rows first, buttom to top
                    grid[j][i] = grid[j][i+1] + grid[j+1][i]
            
            print(grid)

            return grid[0][0]




        return Solution2(m,n)