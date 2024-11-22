class MyCalendar:
    # https://leetcode.com/problems/my-calendar-i/?envType=daily-question&envId=2024-11-22

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        for sTime, eTime in self.calendar:
            if not(startTime >= eTime or endTime <= sTime):
                # overlaping
                return False

        self.calendar.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)