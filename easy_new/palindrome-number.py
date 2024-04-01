class Solution:
    def isPalindrome(self, x: int) -> bool:
        # https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
        
        x_str = str(x)
        x_str = list(x_str)
        x_str_rev = reversed(x_str)
        x_str_rev = "".join(x_str_rev)  

        if x_str_rev == str(x):
            return True
        else:
            return False

