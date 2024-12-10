class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # https://leetcode.com/problems/word-break-ii/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # backtrack only O(2^n)
        wordDict = set(wordDict)

        def backtrack(i):
            
            if i >= len(s):
                ans.append(" ".join(cur))

            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    cur.append(s[i:j+1])
                    backtrack(j+1)
                    cur.pop()
            

        cur = []
        ans = []
        backtrack(0)

        return ans