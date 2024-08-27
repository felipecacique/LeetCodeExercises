class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time o(m+n). Jump a column or a row after each iteraction. Inspired in the soluitions tab
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while col >= 0 and row < m:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False