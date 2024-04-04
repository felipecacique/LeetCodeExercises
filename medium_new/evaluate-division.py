class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # https://leetcode.com/problems/evaluate-division/?envType=study-plan-v2&envId=top-interview-150
        # a = 2 * b
        # b = a / 2
        # b = 3 * c
        # c = b / 3
        # a / c => 2 * b / b / 3 => cut bs => 2 / 1/3 = 6 
        # we must replace the queries in a way that it is left with only one variable, 
        # e.g., bs in the example above, so we can cut the letters
        # use graph ??
        # a = 2 * b
        # b = a / 2
        # b = 3 * c
        # c = b / 3
        # d = 2 * a
        # d / b => 2 * a / 3 * c =: 2*a/3*(b/3) +> ...
        # keep the querie[0] replace the querie[1] over and over untill all bases have the same letters

        # create the adj list
        adj = {}
        for i in range(len(equations)):
            adj[equations[i][0]] = adj.get(equations[i][0], []) + [(equations[i][1], values[i])]
            adj[equations[i][1]] = adj.get(equations[i][1], []) + [(equations[i][0], 1/values[i])]
        
        # traverse the adj list looking for a character, then return its coeficient. An as we return in the recurtion, we multiply the coef by the node's coef
        def dfs(node,c):
            if node in visited: return None
            visited.add(node)
            if node[0] == c: 
                return node[1] # we found the letter we were looking for
            for neightbour in adj.get(node[0], []):
                coef = dfs(neightbour,c)
                if coef: return coef * node[1]
            return None

        # call the dfs for each query
        output = [-1] * len(queries)
        for i, (q1, q2) in enumerate(queries):
            if q1 in adj and q2 in adj:
                visited = set()
                coef = dfs((q1,1),q2)
                if coef: output[i] = coef

        return output
