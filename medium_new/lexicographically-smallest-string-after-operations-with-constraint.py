class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        # https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/
        import string 
        s = s.lower()
        alphabet = string.ascii_lowercase
        alphaIndex = {}
        for i, c in enumerate(alphabet):
            alphaIndex[c] = i
        
        # turn the letter to "a", in order, and if cannot, just get the smallest alphabet near to "a"
        output = []
        for c in s:
            need = min(alphaIndex[c], alphaIndex["z"] - alphaIndex[c] + 1)
            if need <= k: # we can turn the letter c into "a" spending need
                k -= need
                output.append("a")
                continue
            elif k > 0:
                newChar = alphabet[alphaIndex[c] - k]
                output.append(newChar)
                k = 0
            else:
                output.append(c)

        return "".join(output)
