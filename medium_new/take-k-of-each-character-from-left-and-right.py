class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/?envType=daily-question&envId=2024-11-20
        # O(n)

        if k == 0: return 0

        left = -1
        right = len(s) - 1
        freq = {'a':0, 'b':0, 'c':0}
        ans = float('inf')

        def checkSol(freq):
            return freq['a'] >= k and freq['b'] >= k and freq['c'] >= k

        while left < len(s)-1: # add all the left char until find a posssible solution
            left += 1
            freq[s[left]] = freq.get(s[left], 0) + 1 # add the left char
            if checkSol(freq): 
                ans = min(ans, sum(freq.values()))
                break
            
        if not checkSol(freq):
            return -1

        while right >= 0:
            if checkSol(freq): ans = min(ans, sum(freq.values()))
            freq[s[right]] = freq.get(s[right], 0) + 1 # add the right char
            right -= 1

            # now we move the left pointer to the left, removing char from char from freq, until the condition is not valid anymore
            while left >= 0 and checkSol(freq):
                ans = min(ans, sum(freq.values()))
                freq[s[left]] = freq.get(s[left], 0) - 1
                left -= 1

        return ans if ans != float('inf') else -1
        