class Solution:
    def minChanges(self, s: str) -> int:
        # https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/?envType=daily-question&envId=2024-11-05
        ans = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                ans += 1
        return ans