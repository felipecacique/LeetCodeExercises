class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/?envType=daily-question&envId=2024-11-22
        # O(m*n)
        m, n = len(matrix), len(matrix[0])
        ans = 0

        table = {}
        for row in range(m):
            row_str = tuple(matrix[row])
            table[row_str] = table.get(row_str,0) + 1

        for row in range(m):
            flips = [0] * n 
            for col in range(n):
                if matrix[row][col] == 1: flips[col] = 1

            flips_str = tuple(flips)
            flips_inverse_str = tuple([(1 if f == 0 else 0) for f in flips])

            # instead of checking cell by cell, we look of a row partern in table. O(1) lookup of each row
            rowsEqual = 0
            if flips_str in table: rowsEqual += table[flips_str]
            if flips_inverse_str in table: rowsEqual += table[flips_inverse_str]


            # for r in range(m):
            #     count = 0
            #     for c in range(n):
            #         if matrix[r][c] == 1 and flips[c] or matrix[r][c] == 0 and not flips[c]:
            #             count += 1
            #     if count == n or count == 0:
            #         rowsEqual += 1

            ans = max(ans, rowsEqual)   
    
        return ans


# class Solution:
#     def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         ans = 0
#         for row in range(m):
#             flips = [False] * n 
#             for col in range(n):
#                 if matrix[row][col] == 1: flips[col] = True

#             rowsEqual = 0
#             for r in range(m):
#                 count = 0
#                 for c in range(n):
#                     if matrix[r][c] == 1 and flips[c] or matrix[r][c] == 0 and not flips[c]:
#                         count += 1
#                 if count == n or count == 0:
#                     rowsEqual += 1

#             ans = max(ans, rowsEqual)   
    
#         return ans

