class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan-v2&envId=leetcode-75
        # do a bfs O(n)

        from collections import deque
        queue = deque([(0, entrance[0], entrance[1])])
        maze[entrance[0]][entrance[1]] = "v" # visited
        while queue:
            h, y, x = queue.popleft()
            if maze[y][x] == "v" and (y,x) != (entrance[0], entrance[1]) and (y == 0 or y == len(maze)-1 or x == 0 or x == len(maze[0])-1):
                return h
            for y, x in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if y >= 0 and y < len(maze) and  x >= 0 and x < len(maze[0]) and maze[y][x] == ".":
                    queue.append((h+1,y,x))
                    maze[y][x] = "v"
        return -1
            

