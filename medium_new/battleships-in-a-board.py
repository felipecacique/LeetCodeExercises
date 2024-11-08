class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # https://leetcode.com/problems/battleships-in-a-board/
        # time O(n) space O(1) with one-pass
        
        m = len(board)
        n = len(board[0])

        battleships = 0

        for row in range(m):
            for col in range(n):
                if board[row][col] == "X" and (col == 0 or board[row][col-1] == ".") and (row == 0 or board[row-1][col] == "."):
                    battleships += 1
   
        return battleships
