# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # My fist idea is taveling the string both from start to midle, and from end to midle, simultaneosly, comparing the char. If they all match, then it is a palindrome. We can work with a linked list.

        # removing non-alphanumeric characters and lowing case
        import re

        s = s.replace("_", " ")
        s = re.sub(r"\W+", "", s)
        s = s.lower()

        i = 0  # ponts to the start
        j = len(s) - i - 1  # points to the end

        import math

        middle = math.ceil(
            len(s) / 2
        )  # round ceil makes the code work for even size array
        for i in range(0, middle):
            j = len(s) - i - 1
            if s[i] != s[j]:  # it is a match
                return False

        return True
