class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # https://leetcode.com/problems/minimum-time-to-make-rope-colorful/submissions/1338604262/
        # use 2 pointes, pointin to the stratr and end of a sequence. As we itereate, we pop all ballons, but as we finish a sequence, we must put it back the maximum baloon( cuz we shouldn have pop it)
        colors += "."
        neededTime.append(0)
        totalTime = 0
        sequenceColor = colors[0]
        maxTime = neededTime[0]
        for end in range(len(colors)):

            totalTime += neededTime[end]

            if sequenceColor != colors[end]:
                # we have a new sequence
                sequenceColor = colors[end]
                totalTime -= maxTime
                maxTime = neededTime[end]
            
            maxTime = max(maxTime, neededTime[end])
            
        return totalTime