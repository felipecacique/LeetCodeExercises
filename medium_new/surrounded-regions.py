class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
        # i cannot flip if a region is on the edge, othewise i can flip it
        # we must identify the reagions on the border
        # do a bfs or dfs starting from the bourders
        
        m = len(board)
        n = len(board[0])

        stack = []
        seen = set()
        # add bourders 'O'
        for j in range(m):
            for i in range(n):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    if board[j][i] == "O":
                        stack.append((j,i))

        while stack:   
            j, i = stack.pop()
            board[j][i] = "R"
            
            if i+1 < n and (j,i+1) not in seen and board[j][i+1] == "O":
                stack.append((j,i+1)) # this is a neightbour of an unflipped region
                seen.add((j,i+1))
            if i-1 >= 0 and (j,i-1) not in seen and board[j][i-1] == "O":
                stack.append((j,i-1)) # this is a neightbour of an unflipped region
                seen.add((j,i-1))
            if j+1 < m and (j+1,i) not in seen and board[j+1][i] == "O":
                stack.append((j+1,i)) # this is a neightbour of an unflipped region
                seen.add((j+1,i))
            if j-1 >= 0 and (j-1,i) not in seen and board[j-1][i] == "O":
                stack.append((j-1,i)) # this is a neightbour of an unflipped region
                seen.add((j-1,i))
            

        for j in range(m):
            for i in range(n):
                if board[j][i] == "R": board[j][i] = "O"
                else: board[j][i] = "X"


