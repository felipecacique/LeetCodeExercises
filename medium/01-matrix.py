# https://leetcode.com/problems/01-matrix/description/


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Solution1:  we have a graph. we can do a breadth first search from each node, and calculate the height until find an 0. That is the distance for that given node. This approach is too slow O((m*n)^2)

        # Solution2: propagate the zeroes like waves. Like those temperature dissipation graphs. Temperature graph. We will do a bfs, starting from adding all zeroes to the queue first, and then propagate the incremental distance. It will allow we update the whole distance graph 1 by 1 after each iteraction. In the first iteration all nodes that has a distance of 1 will be updates. In the second iteration all nodes that has a distance of 1 will be updated, and so on, untill there is not node left. This will ensure the correcteness. time O(m*n) space(m*n)

        def Solution2(mat):
            m = len(mat)
            n = len(mat[0])
            distances = [[0 for i in range(0, n)] for j in range(0, m)]

            visited = set()
            from collections import deque

            queue = deque()

            # add all the zeroes in the queue first. Our distance count will start from the zeroes, and at each iteretion it will increase by one
            for i in range(0, m):
                for j in range(0, n):
                    if mat[i][j] == 0:
                        queue.append((i, j, 0))
                        visited.add((i, j))

            # now we do a bfs from the zeroes already in the queue
            while 1:
                if len(queue) == 0:
                    break
                coord = queue.popleft()

                i, j, distance = coord
                distances[i][j] = distance

                if i - 1 >= 0 and not (i - 1, j) in visited:
                    queue.append((i - 1, j, distance + 1))
                    visited.add((i - 1, j))
                if i + 1 < m and not (i + 1, j) in visited:
                    queue.append((i + 1, j, distance + 1))
                    visited.add((i + 1, j))
                if j - 1 >= 0 and not (i, j - 1) in visited:
                    queue.append((i, j - 1, distance + 1))
                    visited.add((i, j - 1))
                if j + 1 < n and not (i, j + 1) in visited:
                    queue.append((i, j + 1, distance + 1))
                    visited.add((i, j + 1))

            return distances

        return Solution2(mat)
