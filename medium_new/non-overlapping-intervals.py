class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # supose thet is an overlapping 1 to 1. Then we can just remove any of them. If there is an interval that is overlapping to 2 or more, we must remove this interval
        # we can go greedy, and scan the whole intervals
        # what is non overlapping? it is when the end(i) is smaller or equal to start(i+1), otherwise there is an overlapping
        # we must sort by the end, then we can go greedy

        def Solution1():
            nonOverlapping = []
            overlapping = 0
        
            sortedIntervals = sorted(intervals, key=lambda x: (x[1], x[0]))

            nonOverlapping.append(sortedIntervals[0])

            for i in range(1, len(sortedIntervals)):
                if nonOverlapping[-1][1] <= sortedIntervals[i][0]: # non overlapping
                    nonOverlapping.append(sortedIntervals[i])
                else: # overlapping
                    overlapping += 1

            return overlapping
        
        def Solution2():
            # using pointers intead of a nonOverlapping array
            
            overlapping = 0
            sortedIntervals = sorted(intervals, key=lambda x: (x[1], x[0]))
            j = 0 # poits to the last nonoverlapping interval

            for i in range(1, len(sortedIntervals)):
                if sortedIntervals[j][1] <= sortedIntervals[i][0]: # non overlapping
                    j = i
                else: # overlapping
                    overlapping += 1

            return overlapping

        return Solution2()



