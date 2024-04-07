class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/course-schedule-ii/?envType=study-plan-v2&envId=top-interview-150

        output = []
        seen = set()
        cycle = set()

        adj = {} # created adj list 
        for prer in prerequisites:
            adj[prer[0]] = adj.get(prer[0], []) + [prer[1]]

        def canMakeIt(key):
            if key in cycle: return False # to avoid infinite loops
            if key in seen: return True # memoization
            if key not in adj: # we can make it, base case
                seen.add(key), output.append(key)
                return True
            
            cycle.add(key) # to avoid infinite loops
            for course in adj[key]:
                if not canMakeIt(course): return False
            if not key in seen: 
                seen.add(key), output.append(key)
            cycle.remove(key)
            return True

        for course in range(numCourses):
            if not canMakeIt(course): # we we check if we can make this course, we are sotiong the sequence of courses (output)
                return []

        return output
        
