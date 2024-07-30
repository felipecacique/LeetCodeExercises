class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # https://leetcode.com/problems/license-key-formatting/submissions/1337858406/
        
        s = s.upper()
        s = s.replace("-", "")
        n = len(s)
        
        groups = n//k
        first = n % k
        
        output = ""
        
        if first != 0:
            output += s[:first] + "-"
        
        for i in range(groups):
            start = first + i*k
            output += s[start:start+k] + "-"
        
        return output[:-1]
    