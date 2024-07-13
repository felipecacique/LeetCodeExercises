class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # https://leetcode.com/problems/set-matrix-zeroes/submissions/1319968610/?envType=study-plan-v2&envId=top-interview-150
        
        m = len(matrix)
        n = len(matrix[0])

        zeroes_col = set() # stores the col indexes that has zeroes
        zeroes_row = set() # stores the row indexes that has zeroes
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes_col.add(i)
                    zeroes_row.add(j)
        
        # If there is a zero in that column or row, we replace the cel with zero
        for i in range(m):
            for j in range(n):
                if i in zeroes_col or j in zeroes_row:
                    matrix[i][j] = 0
