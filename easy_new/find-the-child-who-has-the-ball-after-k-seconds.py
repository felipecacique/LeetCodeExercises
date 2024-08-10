class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/
        i = k % (n-1)
        toRight = True if int(k / (n-1)) % 2 == 0 else False
        if toRight: 
            return i
        else:
            return n-1-i