class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # https://leetcode.com/problems/convert-date-to-binary/description/
        date = date.split("-")

        for i in range(len(date)):
            date[i] = bin(int(date[i]))[2:]
        
        return "-".join(date)