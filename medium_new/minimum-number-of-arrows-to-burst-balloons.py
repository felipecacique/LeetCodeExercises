class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=leetcode-75
        # same solution as non-overlapping-intervals
        # go greedy, shoot at the most overlapping first, till there is no more overlapping, ad then we shot a t indivisual baloons
        # points = [[1,5], [4,7], [3,10]]
        # i = 0:  non  j = i = 0, arrow = 0
        # i = 1:  over, remove point[i], keep j pointing to the prev non overlapping point, j = 0 arrow = 0
        # i = 2:  over, remove point[i], keep j pointing to the prev non overlapping point, j = 0 arrow = 0

        # points = [[1,5], [4,7], [6,10]]
        # i = 0:  non  j = i = 0, arrow = 0
        # i = 1:  over, remove point[i], keep j pointing to the prev non overlapping point, j = 0 arrow = 0
        # i = 2:  non j = i = 2, arrow = 2


        points = sorted(points, key=lambda x: (x[1], x[0]))
        arrowCount = 1
        j = 0
        for i in range(1,len(points)):
            if points[j][1] < points[i][0]: # non overlapping
                j = i   # points to the last non overlapping point
                arrowCount+=1
            else: # overlapping
                pass # we do not count arrow
        
        return arrowCount





