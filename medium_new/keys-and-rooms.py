class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # https://leetcode.com/problems/keys-and-rooms/?envType=study-plan-v2&envId=leetcode-75
        # it is a graph problem. Lets create an adjacency list, a bfs and see it we can vist all nodes. For that we will use queue, and a set with all nodes already visited, so we only visit each node once

        visited = set()
        from collections import deque
        queue = deque()
        queue.append(0)
        visited.add(0)

        while queue:
            room = queue.popleft()
            keys = rooms[room]
            for key in keys:
                if not key in visited:
                    queue.append(key)
                    visited.add(key)

        if len(visited) == len(rooms):
            return True
        else:
            False
            





