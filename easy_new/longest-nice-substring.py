class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # https://leetcode.com/problems/longest-nice-substring/
        # brute force solution 
        longest = ""
        for i in range(len(s)):
            substringLetters = set()
            for j in range(i,len(s)):
                substringLetters.add(s[j])
                # check if the substring s[i:j] is NICE. If all letter have its UPPER pairs, then it is NICE
                isNice = True
                for letter in s[i:j+1]:
                    if letter.swapcase() not in substringLetters:
                        isNice = False
                        break
                    # since we found mached for all words, we have a NICE string
                if isNice and len(s[i:j+1]) > len(longest):
                    longest = s[i:j+1]
        return longest