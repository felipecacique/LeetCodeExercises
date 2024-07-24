class RangeModule:
    # https://leetcode.com/problems/range-module/description/
    def __init__(self):
        self.intervals = [[float("-inf"), float("-inf")], [float("inf"), float("inf")]]
        

    def addRange(self, left: int, right: int) -> None:
        # Time complexity O(2*n)
        # Compute the new merged interval andd drop the merged ones
        newIntervals = []
        for i in range(len(self.intervals)):
            left_i, right_i = self.intervals[i][0], self.intervals[i][1]
            if (right < left_i) or (left > right_i): newIntervals.append([left_i, right_i]) # intervals do not merge
            else: left, right = min(left, left_i), max(right, right_i) # intervals overlap
        newInterval = [left, right]
        self.intervals = newIntervals

        # Add the new merged interval to the intervals list
        newIntervals = [[float("-inf"), float("-inf")]]
        for i in range(1,len(self.intervals)):
            if newInterval[0] > self.intervals[i-1][1] and newInterval[1] < self.intervals[i][0]: 
                newIntervals.append(newInterval)
            newIntervals.append(self.intervals[i])

        self.intervals = newIntervals


    def queryRange(self, left: int, right: int) -> bool:
        # Binary search to find the interval O(logn)
        start = 1
        end = len(self.intervals)-2
        middle = 1
        while start <= end:
            middle = (start+end)//2
            if left > self.intervals[middle][0]:
                start = middle + 1
            elif left < self.intervals[middle][0]:
                end = middle - 1
            else: 
                break
        # the middle points to the start of a possible maching interval
        if left >= self.intervals[middle][0] and right <= self.intervals[middle][1]:
            return True
        if left >= self.intervals[start][0] and right <= self.intervals[start][1]:
            return True
        if left >= self.intervals[end][0] and right <= self.intervals[end][1]:
            return True
        return False
        

        return False

    def removeRange(self, left: int, right: int) -> None:
        # Time complexity O(2*n)
        # Compute the new merged interval andd drop the merged ones
        newIntervals = []
        for i in range(len(self.intervals)):
            left_i, right_i = self.intervals[i][0], self.intervals[i][1]
            if (right < left_i) or (left > right_i): 
                newIntervals.append([left_i, right_i]) # intervals do not merge
            else: 
                if left > left_i and right < right_i: # split the same interval in 2 intervals
                    newIntervals.append([left_i, left]) 
                    newIntervals.append([right, right_i])
                elif left > left_i: # cut the interval but do not split in 2, only decrease its range
                    newIntervals.append([left_i, left]) 
                elif right < right_i: # cut the interval but do not split in 2, only decrease its range
                    newIntervals.append([right, right_i]) 
        self.intervals = newIntervals


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)