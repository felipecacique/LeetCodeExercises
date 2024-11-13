class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # https://leetcode.com/problems/day-of-the-week/
        import datetime
        w = datetime.datetime(year, month, day).weekday()
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[w]