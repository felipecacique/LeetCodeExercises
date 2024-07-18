class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # https://leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=top-interview-150
        # calculate the parameters (a and b) of the line between every 2 poins, such that a*x+b=y. Pins in the same line will have same parameters. Then the pair (a,b) that repeated the most is the answer
        # time complexity O(n^2)

        output = 0
        for i in range(len(points)):
            lineParameters = {}
            for j in range(i+1, len(points)):
                # Calculate the parameters of the line between these 2 points
                if (points[i][0] - points[j][0]) != 0:
                    a = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) # a = (y2-y1) / (x2-x1)
                    b = points[i][1] - a * points[i][0] # b = y-a*x
                else:
                    a = float("inf")
                    b = points[i][0]

                lineParameters[(a,b)] = lineParameters.get((a,b), 0) + 1
                output = max(output, lineParameters[(a,b)])

        return output+1