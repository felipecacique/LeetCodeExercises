# https://leetcode.com/problems/longest-palindromic-substring/submissions/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # find the mirror indexes, and expand from there. Time O(n^2)

        def Solution1():
            n = len(s)

            if n == 0: return ""

            # maxPalindrome = [s[0],1]
            maxPalindrome = [(0,1),1] # maxPalindrome[0] holds the start and and indexes of the palindrome, and maxPalindrome[1] holds the size

            for i in range(0, n):
                print(maxPalindrome)
                if i-1 >= 0 and s[i-1] == s[i]: # we have found a mirror point, the middle of an even palindrome
                    j = 2
                    while i-j >= 0 and i+j-1 < n and s[i-j] == s[i+j-1]:
                        j += 1
                    
                    size = (j-1) * 2
                    if size > maxPalindrome[1]:
                        maxPalindrome[1] = size
                        # maxPalindrome[0] = s[i-j+1 : i+j-1-1+1] # holds the longets palindrome
                        maxPalindrome[0] = (i-j+1, i+j-1-1+1) # holds the longets palindrome

                
                if i-1 >= 0 and i+1<n and s[i-1] == s[i+1]: # we have found a mirror point, the middle of an odd palindrome
                    j = 2
                    while  i-j >= 0 and i+j<n and s[i-j] == s[i+j]: # compare the mirrowed chars in the palindrome. If they are different, then stop
                        j += 1
                    
                    size = (j-1) * 2 + 1
                    if size > maxPalindrome[1]:
                        maxPalindrome[1] = size
                        # maxPalindrome[0] = s[i-j+1 : i+j-1+1] # holds the longets palindrome
                        maxPalindrome[0] = (i-j+1, i+j-1+1) # holds the longets palindrome
        
            # return maxPalindrome[0]
            return s[maxPalindrome[0][0] : maxPalindrome[0][1]]
        
        def Solution2():
            # i redone this squestion 3 months later than the solution1

            if not s:
                return ""

            maxLen = 1
            palindrome = (0,1)
            
            # odd len
            for i in range(0,len(s)):
                for j in range(0,i+1):
                    if i-j < 0 or i+j+1 > len(s): break
                    if s[i-j] != s[i+j]: break
                    if 2*j+1 > maxLen: palindrome, maxLen = (i-j,i+j+1), 2*j+1 

            # even len
            for i in range(0,len(s)):
                for j in range(0,i+1):
                    if i-j < 0 or i+j+2 > len(s): break
                    if s[i-j] != s[i+j+1]: break
                    if 2*j+2 > maxLen: palindrome, maxLen = (i-j,i+j+2), 2*j+2
                            
            return s[palindrome[0]:palindrome[1]]


        return Solution1()