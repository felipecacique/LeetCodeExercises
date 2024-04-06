class Solution:
    def romanToInt(self, s: str) -> int:
        # https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
        roman_to_int = {'I': 1, 'V': 5, "X": 10, "L":50, "C":100, "D": 500, "M": 1000}
        s = list(reversed(s))
        number = 0
        last = 'I'
        for i in range(len(s)):
            print()
            if s[i] == "I" and last in ['V', 'X']:
                number -= roman_to_int[s[i]]
            elif s[i] == "X" and last in ['L', 'C']:   
                number -= roman_to_int[s[i]]
            elif s[i] == "C" and last in ['D', 'M']: 
                number -= roman_to_int[s[i]]
            else:
                number += roman_to_int[s[i]]

            last = s[i]

        return number
