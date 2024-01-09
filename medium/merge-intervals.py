# https://leetcode.com/problems/merge-intervals/submissions/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) for the sorting

        intervals.sort() # sort by start 

        output = [intervals[0]]

        for interval in intervals[1:]:

            if interval[0] > output[-1][1]: # no overlapping 
                output.append(interval) # we just add the new interval there
            else:  # overlapping
                # lets merge the overlapping interval
                output[-1] = [ min(output[-1][0], interval[0]), max(output[-1][1], interval[1]) ] # merge the overlapping
        
        return output