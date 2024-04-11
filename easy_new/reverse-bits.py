class Solution:
    def reverseBits(self, n: int) -> int:
        # https://leetcode.com/problems/reverse-bits/submissions/1228990587/?envType=study-plan-v2&envId=top-interview-150
        res = 0
        for _ in range(32):
            bit = n & 1
            res = res << 1
            res = res | bit
            n = n >> 1
        return res