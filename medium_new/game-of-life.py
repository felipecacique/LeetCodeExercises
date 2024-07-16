class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150

        seen = {}
        m = len(board)
        n = len(board[-1])

        for i in range(m):
            for j in range(n):
                
                neighbours = []
                for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1), (i+1,j+1), (i-1,j-1), (i-1,j+1), (i+1,j-1)]:
                    if a >= 0 and a < m and b >= 0 and b < n:
                        if (a,b) in seen: neighbour = seen[(a,b)]
                        else: neighbour = board[a][b]
                        neighbours.append(neighbour)

                seen[(i,j)] = board[i][j]

                sumNeighbours = sum(neighbours)
                if board[i][j] == 1 and sumNeighbours < 2: board[i][j] = 0
                elif board[i][j] == 1 and sumNeighbours in [2, 3]: board[i][j] = 1
                elif board[i][j] == 1 and sumNeighbours > 3 : board[i][j] = 0
                elif board[i][j] == 0 and sumNeighbours == 3 : board[i][j] = 1

                
