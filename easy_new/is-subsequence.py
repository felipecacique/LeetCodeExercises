class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
        # use pointers

        if len(s) == 0:
            return True

        a = 0 # points to t
        b = 0 # poits to s

        while a <= len(t)-1:
            if t[a] == s[b]:
                b += 1
                if b >= len(s):
                    return True
            a += 1
        return False



