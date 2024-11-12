class Solution:
    def reverse(self, x: int) -> int:
        # https://leetcode.com/problems/reverse-integer/
        maxnum = 2**31 - 1
        minnum = -2**31
        if x >= 0: 
            ans = int(str(x)[::-1])
            return ans if ans <= maxnum else 0 
        else: 
            ans = -int(str(x*-1)[::-1])
            return ans if ans >= minnum else 0 