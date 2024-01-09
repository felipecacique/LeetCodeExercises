# https://leetcode.com/problems/flood-fill/description/


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def Solution1(image, sr, sc, color):
            # lets model it as a graph problem where each pixel is connected 4-directionally to the starting pixel of the same color as the starting pixel. And for doing the coloring we wil performa a BFS or DFS to vitit all the connected nodes, and as e travel through them, we change its colors. Adjacency list implementation. time O(m*n) space O(m*n)

            # create the graph (harsh table)
            graph = {}

            for i in range(0, len(image)):
                if len(image[0]) > 0:
                    for j in range(0, len(image[0])):
                        edges = []

                        if i + 1 >= 0 and i + 1 < len(image):  # if pixel exists
                            if (
                                image[i][j] == image[i + 1][j]
                            ):  # it they have the same color
                                edges.append(
                                    (i + 1, j)
                                )  # then we add it to the connections list

                        if i - 1 >= 0 and i - 1 < len(image):  # if pixel exists
                            if (
                                image[i][j] == image[i - 1][j]
                            ):  # it they have the same color
                                edges.append(
                                    (i - 1, j)
                                )  # then we add it to the connections list

                        if j + 1 >= 0 and j + 1 < len(image[0]):  # if pixel exists
                            if (
                                image[i][j] == image[i][j + 1]
                            ):  # it they have the same color
                                edges.append(
                                    (i, j + 1)
                                )  # then we add it to the connections list

                        if j - 1 >= 0 and j - 1 < len(image[0]):  # if pixel exists
                            if (
                                image[i][j] == image[i][j - 1]
                            ):  # it they have the same color
                                edges.append(
                                    (i, j - 1)
                                )  # then we add it to the connections list

                        graph[(i, j)] = edges

            # now that we have our graph, lets travel it

            visited = {}

            def dfs(node):  # the node here is the pair (i,j)
                if node in visited:  # we have already visited this node
                    return

                i, j = node[0], node[1]
                image[i][j] = color  # we color the node we visit

                visited[node] = True  # add the node to the visited nodes

                for edge in graph[node]:  # we will visit all adges of node
                    dfs(edge)

                return

            root = (sr, sc)
            dfs(root)

            return image

        def Solution2(image, sr, sc, color):
            # similar to solution1 but we wont create the adjacency list. We will travel the graph directly. It is faster because we do not have to create the whole graph.

            visited = {}
            m, n = len(image), len(image[0])

            def dfs(node):  # the node here is the pair (i,j)
                if node in visited:  # we have already visited this node
                    return

                # find edges
                edges = []
                i, j = node[0], node[1]

                if i + 1 < m:  # if pixel exists
                    if image[i][j] == image[i + 1][j]:  # it they have the same color
                        edges.append(
                            (i + 1, j)
                        )  # then we add it to the connections list

                if i - 1 >= 0:  # if pixel exists
                    if image[i][j] == image[i - 1][j]:  # it they have the same color
                        edges.append(
                            (i - 1, j)
                        )  # then we add it to the connections list

                if j + 1 < n:  # if pixel exists
                    if image[i][j] == image[i][j + 1]:  # it they have the same color
                        edges.append(
                            (i, j + 1)
                        )  # then we add it to the connections list

                if j - 1 >= 0:  # if pixel exists
                    if image[i][j] == image[i][j - 1]:  # it they have the same color
                        edges.append(
                            (i, j - 1)
                        )  # then we add it to the connections list

                # we color the node after we get all its edges
                i, j = node[0], node[1]
                image[i][j] = color  # we color the node we visit

                visited[node] = True  # add the node to the visited nodes

                for edge in edges:  # we will visit all adges of node
                    dfs(edge)

                return

            root = (sr, sc)
            dfs(root)

            return image

        return Solution2(image, sr, sc, color)
