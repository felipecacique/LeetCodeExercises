class Solution:
    def totalNQueens(self, n: int) -> int:
        # https://leetcode.com/problems/n-queens-ii/?envType=study-plan-v2&envId=top-interview-150
        # there must only be one queen per row and 1 queen per line
        # exp: n = 4 column=[0, 1, 2, 3]  row=[1, 3, 0, 2]  where the index represent that specific queen piece
        # time complexity O(n!)

        def Solution1():
             # we can fux que column vector, and just think about the row array. We do a permutation of row and as we do we check if that permutation is valid (if the queen does no attack each other)
            ans = [0]
            def backtrack(perm, notAllowedPos):
                if len(perm) == n:
                    ans[0] += 1
                    return
                for row in range(n):
                    col = len(perm) 
                    notAllowedPos_copy = notAllowedPos.copy()
                    if not (col, row) in notAllowedPos_copy: # does not allow queens to be at the same row and diagonal (otherwise they would attack each other)
                        for c in range(col,n): notAllowedPos_copy.add((c,row)) # since we add a new queen, add the prohibitted cells for the new queens (same row and diagonal)
                        for i in range(min(n-col, n-row)): notAllowedPos_copy.add((col+i,row+i)) # prohibited diagonals
                        for i in range(min(n-col, row+1)): notAllowedPos_copy.add((col+i,row-i)) # prohibited diagonals
                        backtrack(perm+[row], notAllowedPos_copy)
                        
            backtrack([], set())
            return ans[0]

        def Solution2():
            # cleaner and faster. Inspired in one of the submissions solutions
            ans = 0
            rowProhib = set()
            diagPosProhib = set()
            diagNegProhib = set()
            def backtrack(col):
                nonlocal ans
                if col == n:
                    ans += 1
                    return
                for row in range(n):
                    if row not in rowProhib and row+col not in diagPosProhib and row-col not in diagNegProhib:
                        rowProhib.add(row)
                        diagPosProhib.add(row+col)
                        diagNegProhib.add(row-col)
                        backtrack(col+1)
                        rowProhib.remove(row)
                        diagPosProhib.remove(row+col)
                        diagNegProhib.remove(row-col)
                        
            backtrack(0)
            return ans
        
        return Solution2()