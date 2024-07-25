class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # https://leetcode.com/problems/repeated-dna-sequences/
        # O(n*10)
        seen = set()
        output = set()
        for i in range(10,len(s)+1):
            subsequence = s[i-10:i]
            if subsequence in seen: output.add(subsequence)
            else: seen.add(subsequence)
        return output