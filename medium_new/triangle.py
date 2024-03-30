class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def SolutionToDown():
            dp = {}

            def dfs(h,i):

                if (h,i) in dp:
                    return dp[(h,i)]

                if h == len(triangle[-1])-1: # reached the end of the triangle
                    return triangle[h][i]
                
                leftBestPath = dfs(h+1,i) + triangle[h][i]
                rightBestPath = dfs(h+1,i+1) + triangle[h][i]

                bestPath = min(leftBestPath, rightBestPath)

                dp[(h,i)] = bestPath

                return bestPath

            return dfs(0,0)

        def SolutionBottomUp():

            for i in range(len(triangle)-2, -1, -1):
                for j in range(len(triangle[i])):
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
            return triangle[0][0]

        return SolutionBottomUp()