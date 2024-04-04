class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
        reminder = 1
        for i in range(len(digits)-1, -1, -1):
            result = digits[i] + reminder
            digits[i] = result%10
            reminder = result//10
        if reminder == 1: digits = [1] + digits
        return digits