class Solution:
    # https://leetcode.com/problems/pascals-triangle/
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]

        pascal = [[1], [1,1]]
        for i in range(2, numRows):
            new = [1] * (i+1)
            for j in range(len(pascal[i-1])-1):
                new[1+j] = pascal[i-1][j] + pascal[i-1][j+1]
            pascal.append(new)
        return pascal
