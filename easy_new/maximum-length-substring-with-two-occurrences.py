class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/submissions/1350414496/
        l = 0
        charCount = {}
        output = 0
        for r in range(len(s)):
            c = s[r]
            charCount[c] = charCount.get(c, 0) + 1

            while charCount[c] > 2 and l < r:
                # the substring is not valid, so lets shrink it untill it becomes valig again
                charCount[s[l]] -= 1
                l += 1
            
            output = max(output, r-l+1)

        return output
