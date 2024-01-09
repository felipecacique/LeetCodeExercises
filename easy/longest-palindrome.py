# https://leetcode.com/problems/longest-palindrome/description/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # to be an palindrome the sum of all letters must be even, except one that can be odd(in case the word's lenth is odd, and there is a single letter in the middle). Lets count how many every letter appers in the string, For each pair of a single letter, they can be added in the palindrome. O(n)

        counLetters = {}

        for letter in s:
            if not letter in counLetters:
                counLetters[letter] = 1
            else:
                counLetters[letter] += 1

        pairs = 0
        reminder = 0
        for letter, count in counLetters.items():
            pairs += int(count / 2)
            reminder += count % 2

        if reminder == 0:
            return pairs * 2

        else:  # since we have letter left, we can get one of them and place it in the middle of the palindrome, making it longer
            return pairs * 2 + 1
