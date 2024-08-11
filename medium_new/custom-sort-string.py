class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # https://leetcode.com/problems/custom-sort-string/
        charFreq = {}
        for c in s:
            charFreq[c] = charFreq.get(c, 0) + 1
        
        sol = []
        for c in order:
            while c in charFreq and charFreq[c]>0:
                sol.append(c)
                charFreq[c] -= 1
            
        for c in s: # add the remaining char
            if charFreq[c] > 0:
                sol.append(c)
        
        return "".join(sol)