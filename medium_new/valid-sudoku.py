class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # https://leetcode.com/problems/valid-sudoku/submissions/1223156172/?envType=study-plan-v2&envId=top-interview-150
        
        # checking the blocks
        for start1 in [0,3,6]:
            for start2 in [0,3,6]:
                seen = set()
                for j in range(start1,start1+3):
                    for i in range(start2,start2+3):
                        if board[j][i] != '.':
                            if not board[j][i] in seen:
                                seen.add(board[j][i])
                            else:
                                return False

        # checking the rows
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[j][i] != '.':
                    if not board[j][i] in seen:
                        seen.add(board[j][i])
                    else:
                        return False
                        
        # checking the columns    
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.':
                    if not board[j][i] in seen:
                        seen.add(board[j][i])
                    else:
                        return False

        return True