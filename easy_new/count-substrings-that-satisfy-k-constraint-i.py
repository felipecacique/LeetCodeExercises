class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/
        sol = 0
        for i in range(len(s)):
            count1 = 0
            count0 = 0
            for j in range(i, len(s)):
                c = s[j]
                if c == "1": count1 += 1
                else: count0 += 1
                if count1 <= k or count0 <=k:
                    sol += 1
        return sol

        