# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # https://leetcode.com/problems/guess-number-higher-or-lower/?envType=study-plan-v2&envId=leetcode-75
        # we will do a binary search
        a = 0
        b = n
        while a <= b:
            myGuess = int((a + b)/2)
            if guess(myGuess) == 1: 
                # the solution is on the right
                a = myGuess + 1
            elif guess(myGuess) == -1:
                # the solution is on the left
                b = myGuess - 1
            else:
                return myGuess


