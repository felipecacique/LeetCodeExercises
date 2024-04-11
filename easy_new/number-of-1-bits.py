class Solution:
    def hammingWeight(self, n: int) -> int:
        # https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150
        count = 0
        while n:
            bit = n & 1
            if bit == 1:
                count += bit
            n = n >> 1

        return count