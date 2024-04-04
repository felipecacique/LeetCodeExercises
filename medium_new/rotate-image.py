class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
        
        s = 0
        e = s + len(matrix)-1
        for j in range(len(matrix)//2):
            for i in range(e-s): 
                a, b, c, d =  matrix[s][s+i], matrix[s+i][e], matrix[e][e-i], matrix[e-i][s] 
                matrix[s+i][e], matrix[e][e-i], matrix[e-i][s], matrix[s][s+i] = a, b, c, d
            s = s + 1
            e = e - 1
        