class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # https://leetcode.com/problems/length-of-last-word/?envType=daily-question&envId=2024-04-01
        arr = s.split()
        return len(arr[-1])