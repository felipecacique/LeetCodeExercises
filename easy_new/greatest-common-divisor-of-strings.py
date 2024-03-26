class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
        
        a = str1
        b = str2
        
        while 1:
            if a+b != b+a:
                # it does not have a common divisor
                return ""
            elif len(a) == len(b): 
                return a

            if len(a) > len(b):
                a = a[len(b):] # get the remainder
            elif len(a) < len(b):
                b = b[len(a):] 
            
            #repeat the process, but now with smaller lists (the reminder)
            
            
            