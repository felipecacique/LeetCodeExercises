class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # https://leetcode.com/problems/minimum-area-rectangle/
        # combine every 2 points to be the diagonal edges. Then we know what the values the other points must be. So we look in a harsh table if those point exist. If it is so, we have a retangle
        # O(n^2)

        minArea = float("inf")
        points = sorted(points)
        pointsSet = set([tuple(point) for point in points])
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 < x2 and y1 < y2:
                # if x1 != x2 and y1 != y2: # look for diagonal points (xs and ys must be different)
                    if (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                        retangleArea = abs(x2 - x1) * abs(y2 - y1)
                        minArea = min(minArea, retangleArea)
        return minArea if minArea != float("inf") else 0