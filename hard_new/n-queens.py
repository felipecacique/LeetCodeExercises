class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # https://leetcode.com/problems/n-queens/?envType=study-plan-v2&envId=top-100-liked
        # time O(n^n) space O(n^2)

        output = []
        rowSeen = set()
        diagUpSeen = set()
        diagDownSeen = set()
        
        def backtrack(col, row, sol):
            if col == n:
                # output.append(sol[:])
                # Convert sol[] to the string formart
                solString = [ ['.']*n for _ in range(n) ]
                for col, row in enumerate(sol):
                    solString[col][row] = "Q"
                solString = [ "".join(row) for row in solString ]
                output.append(solString)
                return 

            for row in range(n):
                diagUp = row + col
                diagDown = row - col
                if not row in rowSeen and not diagUp in diagUpSeen and not diagDown in diagDownSeen:
                    rowSeen.add(row)
                    diagUpSeen.add(diagUp)
                    diagDownSeen.add(diagDown)
                    sol.append(row)
                    backtrack(col+1, row, sol)
                    sol.pop()
                    rowSeen.remove(row)
                    diagUpSeen.remove(diagUp)
                    diagDownSeen.remove(diagDown)
        
        backtrack(0, 0, [])
        return output