class MyCalendarTwo:
    # https://leetcode.com/problems/my-calendar-ii/
    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        count = 0
        overlaps = []
        for sTime, eTime in self.calendar:

            for startTime2, endTime2 in overlaps:
                if not(startTime2 >= eTime or endTime2 <= sTime):
                    return False
                
            if not(startTime >= eTime or endTime <= sTime):
                # overlaping
                startTime2 = max(startTime,sTime)
                endTime2 = min(endTime,eTime)
                overlaps.append([startTime2,endTime2])
            
        self.calendar.append([startTime, endTime])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)