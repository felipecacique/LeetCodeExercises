class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
        # we will so a slinding window, with a count, adding a vower from the right and removing a vowel from the left window
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        a = 0
        b = k-1

        count = 0
        max_count = 0
        for i in range(a,b+1):
            if s[i] in vowels:
                count += 1
        max_count = count
        
        # do the sliding window
        a, b = a+1, b+1
        while b < len(s):
            if s[a-1] in vowels:
                count -= 1
            if s[b] in vowels:
                count += 1
            max_count = max(max_count, count)
            a, b = a+1, b+1

        return max_count