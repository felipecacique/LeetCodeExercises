class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
        # Bottom up approach. The idea is using a dp table and iterate starting from the smallest cells to the largest. For eavery cell, we look at its neightbour and see if it is a continuation of a sequence peviously computed.
        # O(m*n*log(m*n)) (to sort)

        # Flatten the matrix, getting the num and coordinates, add to a list, and sort it
        m = len(matrix)
        n = len(matrix[0])
        flattenSorted = []
        for j in range(m):
            for i in range(n):
                flattenSorted.append((matrix[j][i], j, i))
        flattenSorted = sorted(flattenSorted)

        # Create the dynamic programming table storing the max size of the path in which that cell is the head(last element)
        dp = [[0]*n for _ in range(m)]
        maxSize = 0
        for num, j, i in flattenSorted:
            
            if i-1 >= 0 and num > matrix[j][i-1]: dp[j][i] = max(dp[j][i],dp[j][i-1])
            if i+1 < n and num > matrix[j][i+1]: dp[j][i] = max(dp[j][i],dp[j][i+1])
            if j-1 >= 0 and num > matrix[j-1][i]: dp[j][i] = max(dp[j][i],dp[j-1][i])
            if j+1 < m and num > matrix[j+1][i]: dp[j][i] = max(dp[j][i],dp[j+1][i])
            dp[j][i] += 1
            maxSize = max(maxSize, dp[j][i])

        return maxSize