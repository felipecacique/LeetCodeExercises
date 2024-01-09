# https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # we get char by char in s, and ckeck if that word is in wordDict. If it is in there, we have two options. Pop that word from s, or keep it there, because that is not the right word to pop (might be another one that fit better, exp: dog, dogs). Then we will have two branches, we repeat the process for each branch untill there is a branch where we have removed all worlds. Time O(n^2) in worst case. Instead of removing the words, we could use pointers to save memory. And also memoization, saving the information if we have solution for start = start

        have_solution = set() # we ill add here the start/end that we have already solution for

        n = len(s)

        def dfs(start):

            if start >= n: # since the start is pointing to the end of the string, st meand that we have removed all words from it, and must return true
                return True
            
            for i in range(start, n+1):
                if s[start:i] in wordDict: # get a slice of the string
                    # the word is in the dict, so we have tho optitions. Keeping seraching here in this loop for othwe word, or pop the found word and start a new search/branch from there

                    # memoization
                    if not i in have_solution: # avoind exploring multiple times the same branch
                        have_solution.add(i)  
                        
                        if dfs(i) == True: # new branch
                            return True 

            return False

        return dfs(0)
