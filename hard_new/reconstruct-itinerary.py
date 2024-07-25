class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # https://leetcode.com/problems/reconstruct-itinerary/
        # create adj list and do a dfs in preaorder traversal, creating paths with lexical order.

        if not tickets: return [] # edge case

        tickets = sorted(tickets)

        # Create adj list
        adj = {} # start:end
        for ticket in tickets:
            if not ticket[0] in adj: adj[ticket[0]] = {ticket[1]:1}
            else: 
                if not ticket[1] in adj[ticket[0]]: adj[ticket[0]][ticket[1]] = 1
                else: adj[ticket[0]][ticket[1]] += 1

        # do the dfs, and stop as soon we find a path with size len(tickets) + 1 
        output = [[]]
        def createPath(path):
            if len(path) == len(tickets) + 1:
                output[0] = path
                return True

            last = path[-1]
            if last in adj:
                for end in adj[last].keys():
                    if adj[last][end] != 0:
                        adj[last][end] -= 1
                        path.append(end)
                        if createPath(path) == True:
                            return True
                        path.pop()
                        adj[last][end] += 1
            return False

        createPath(["JFK"])

        return output[0]