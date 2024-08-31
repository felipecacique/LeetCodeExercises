class Solution:
    def stringHash(self, s: str, k: int) -> str:
        # https://leetcode.com/problems/hash-divided-string/description/
        def charToInt(char):
            return ord(char) - ord('a')
        
        def intToChar(num):
            return chr(num + ord('a'))

        res = []
        for j in range(0,len(s),k):
            total = 0 
            for i in range(j,j+k):
                total += charToInt(s[i])
            res.append(intToChar(total%26))
        
        return "".join(res)


            