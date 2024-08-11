class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        # https://leetcode.com/problems/count-the-number-of-good-nodes/description/
        from collections import defaultdict
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        print(adj)
        goodNodes = [0]
        seen = set([0])
        def countNodes(node):
            if len(adj[node]) == 1 and adj[node][0] in seen:
                goodNodes[0] += 1
                return 1 # leaf

            sizes = []
            for neighbour in adj[node]:
                if not neighbour in seen:
                    seen.add(neighbour)
                    sizes.append(countNodes(neighbour))

            isGoodNode = True
            if sizes:
                for s in sizes:
                    if s != sizes[0]:
                        isGoodNode = False
            if isGoodNode:
                goodNodes[0] += 1

            return sum(sizes) + 1

        countNodes(0)

        return goodNodes[0]