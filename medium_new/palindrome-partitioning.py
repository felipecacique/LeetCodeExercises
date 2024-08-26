class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # https://leetcode.com/problems/palindrome-partitioning/?envType=study-plan-v2&envId=top-100-liked
        output = []
        def backtrack(r, palin):
            if r == len(s):
                output.append(palin[:])
                return
            for i in range(r,len(s)):
                sub = s[r:i+1]
                if not sub == sub[::-1]: 
                    continue
                palin.append(sub)
                backtrack(i+1,palin)
                palin.pop()
        backtrack(0, [])
        
        return output


