class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # https://leetcode.com/problems/equal-row-and-column-pairs/submissions/1363512017/?envType=study-plan-v2&envId=leetcode-75
        # O(n*n)
        from collections import defaultdict
        rowSet, colSet = defaultdict(int), defaultdict(int)
        for i in range(len(grid)):
            rowSet[tuple(grid[i])] += 1
        
        res = 0
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            if tuple(col) in rowSet: res += rowSet[tuple(col)]
            # colSet[tuple(col)] += 1

        return res