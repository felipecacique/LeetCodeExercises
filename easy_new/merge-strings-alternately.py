class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
        
        i = 0
        merged = ""
        word1Len = len(word1)
        word2Len = len(word2)
        wordMax = max(word1Len, word2Len)

        while i < wordMax:
            if i < word1Len:
                merged += word1[i]
            if i < word2Len:
                merged += word2[i]
            i += 1
    
        return merged