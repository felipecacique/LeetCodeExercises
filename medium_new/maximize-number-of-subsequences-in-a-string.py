class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
        # a good way is to addpattern[0] at the beggining of text, or pattern[1] at the end of text.  Lets count how many pattern[0] and [1] in text. So that we will know what is the best pattern to add
        # time O(n) space (1)
        subsequences = 0
        count1, count2 = 0, 0
        for c in text:
            if c == pattern[1]:
                count2 += 1
                subsequences += count1
            if c == pattern[0]:
                count1 += 1
        
        if count1 >= count2:
            subsequences += count1
        else:
            subsequences += count2
        
        return subsequences
