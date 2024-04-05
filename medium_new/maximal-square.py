class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&envId=top-interview-150
        # dynamic programming O(m*n*n)

        # transforming from str to int
        for j in range(len(matrix)): 
            for i in range(len(matrix[0])):
                 matrix[j][i] = int(matrix[j][i])
                 
        # fill the array with a number indicating the number of 1's it sees above
        for j in range(1,len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[j][i] == 1:
                    matrix[j][i] = matrix[j-1][i] + 1
        
        # use our filled array to calculate the possible 1's squares
        squareSize = 0
        for j in range(0,len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[j][i] > squareSize: # then matrix[j][i] is a candidate
                    # move size-1 positions to the right (where size=matrix[j][i]) and check if we can create a square
                    height = matrix[j][i]
                    length = 0
                    while length < height:
                        # point to the right
                        if i+length >= len(matrix[0]): break # out of bounds
                        height = min(height,matrix[j][i+length])
                        length += 1

                        if height == length and height > squareSize:
                            squareSize = height

        return squareSize ** 2
        
