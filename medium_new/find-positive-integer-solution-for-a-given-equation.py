"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
        sol = []
        for x in range(1, 101):
            for y in range(1, 101):
                if customfunction.f(x,y) == z:
                    sol.append([x,y])
                    break
        
        return sol
        