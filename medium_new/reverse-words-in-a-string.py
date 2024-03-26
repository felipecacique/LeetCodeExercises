class Solution:
    def reverseWords(self, s: str) -> str:
        # https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
        
        arr = list(s.split())[::-1]

        return ' '.join(arr)