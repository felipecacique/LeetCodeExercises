class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/single-number-ii/?envType=study-plan-v2&envId=top-interview-150
        # counting bits ... i saw it in a solution of someone's else

        bit_count = [0] * 32
        for num in nums:
            for i in range(32):
                bit = num & 1
                num = num >> 1
                if bit == 1:
                    bit_count[i] += 1

        ans = 0
        for count in reversed(bit_count):
            if count % 3 == 0:
                ans = ans << 1
            else:
                ans = ans << 1
                ans = ans | 1

        # i got this part from chatgpt to treat overflow, and worked
        if ans > 0x7FFFFFFF:
            ans -= 0x100000000

        return ans