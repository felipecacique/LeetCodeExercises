class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # https://leetcode.com/problems/snakes-and-ladders/description/?envType=study-plan-v2&envId=top-interview-150

        goal = len(board) * len(board[0])
        
        # lets linearize/flatten the board to make the solution easier
        board = [ (row if (len(board)-i-1) % 2 == 0 else list(reversed(row))) for i, row in enumerate(board)]
        board_flat = []
        for row in reversed(board):
            board_flat += row

        from collections import deque
        queue = deque()
        queue.append((1, 0))
        seen = {} # stores the position and the optimum number of moves to reach it
        while queue: # the bfs allows us to search in order of amount of moves, e.g, In the sequence 1, 2, 3 ..... This way, as soon as we reach the goal, that is the smallest amount of moves we need to get there
            pos, moves = queue.popleft()
            for dice in range(1, 7):
                if board_flat[pos+dice-1] != -1: 
                    pos_next = board_flat[pos+dice-1] # follow the latter/snake
                else: 
                    pos_next = pos+dice
                if pos_next == goal: return moves + 1 # check if we reached the goal
                if pos_next not in seen or moves+1 < seen[pos_next]:  # we only explore that path to the pos_next if it is better the previous path to the pos_next
                    queue.append((pos_next, moves+1)) # add the path to the queue
                    seen[pos_next] = moves+1
        return -1
