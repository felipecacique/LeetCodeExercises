class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150
        # binary search O(log(m*n))

        m, n = len(matrix), len(matrix[0])
        def getFromMatrix(idx):
            i = idx % n
            j = idx // n
            return matrix[j][i]
        left, right = 0, m*n-1
        while left <= right:
            middle = (left+right)//2
            if target < getFromMatrix(middle): right = middle-1
            elif target > getFromMatrix(middle): left = middle+1
            else: return True
        return False

