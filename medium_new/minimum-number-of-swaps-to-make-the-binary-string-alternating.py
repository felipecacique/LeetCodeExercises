class Solution:
    def minSwaps(self, s: str) -> int:
        # https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
        # O(n)

        char = "1"
        removed1, removed0 = 0, 0 
        for c in s:
            if c != char:
                if c == "1": removed1 += 1
                elif c == "0": removed0 += 1
            char = "0" if char == "1" else "1"
            
        char = "0"
        removed1_, removed0_ = 0, 0 
        for c in s:
            if c != char:
                if c == "1": removed1_ += 1
                elif c == "0": removed0_ += 1
            char = "0" if char == "1" else "1"

        if removed1 != removed0 and removed1_ != removed0_:
            return -1
        elif removed1 != removed0:
            return removed1_
        elif removed1_ != removed0_:
            return removed1

        return min(removed1, removed1_)