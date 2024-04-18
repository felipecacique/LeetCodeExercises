class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # https://leetcode.com/problems/maximize-distance-to-closest-person/
        
        distFromLeft = [float('-inf')] * len(seats)
        distFromRight = [float('-inf')] * len(seats)
        
        for i in range(0, len(seats)):
            if seats[i] == 1: distFromLeft[i] = 0
            elif i-1 >= 0: distFromLeft[i] = distFromLeft[i-1] + 1
                
        for i in range(len(seats)-1,-1,-1):
            if seats[i] == 1: distFromRight[i] = 0
            elif i+1 < len(seats): distFromRight[i] = distFromRight[i+1] + 1
        
        maxDistance = 0
        for i in range(len(seats)):
            if distFromLeft[i] == distFromRight[i]:
                maxDistance = max(maxDistance, distFromLeft[i])
            elif distFromLeft[i] == float('-inf'):
                maxDistance = max(maxDistance, distFromRight[i])
            elif distFromRight[i] == float('-inf'):
                maxDistance = max(maxDistance, distFromLeft[i])
            elif i+1< len(seats) and distFromLeft[i] + distFromLeft[i+1] == distFromRight[i] + distFromRight[i+1]:
                maxDistance = max(maxDistance, distFromLeft[i])
                
        
        
        return maxDistance