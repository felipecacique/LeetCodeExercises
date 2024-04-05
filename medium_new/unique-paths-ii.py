class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150
        # dynamic programming. Lets use the obstacleGrid itself as our dp table
        for j in range(len(obstacleGrid)-1,-1,-1):
            for i in range(len(obstacleGrid[0])-1,-1,-1):
                if i == len(obstacleGrid[0])-1 and j == len(obstacleGrid)-1 and obstacleGrid[j][i] != 1:
                    obstacleGrid[j][i] = 1 # initalize base case
                elif obstacleGrid[j][i] == 1:
                    obstacleGrid[j][i] = 0  
                else:
                    rightPaths = obstacleGrid[j][i+1] if i+1 < len(obstacleGrid[0]) else 0 # number of different paths from the right
                    downPaths = obstacleGrid[j+1][i] if j+1 < len(obstacleGrid) else 0 # number of different paths from the bottom
                    obstacleGrid[j][i] = rightPaths + downPaths # the number of paths from ij is the the sum of paths if we go right, or down
        return obstacleGrid[0][0]