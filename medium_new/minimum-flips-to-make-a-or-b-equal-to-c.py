class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/?envType=study-plan-v2&envId=leetcode-75
        res = 0
        for _ in range(32):
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
            if bit_c == 0 and bit_a == 1:
                res += 1
            if bit_c == 0 and bit_b == 1:
                res += 1
            if bit_c == 1 and bit_a == 0 and bit_b == 0:
                res += 1
        return res