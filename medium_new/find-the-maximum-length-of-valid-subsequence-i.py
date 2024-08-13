class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/
        # both are even, odd or alternating even with odd
        # go greedy
        
        # both are even, we can just count the ammount of even numbers
        countEven = 0
        for n in nums:
            if n%2 == 0:
                countEven += 1
                
        # both are odd
        countOdd = 0
        for n in nums:
            if n%2 == 1:
                countOdd += 1
        
        # alternating (starting from even)
        cond = 0
        countEvenOdd = 0
        for n in nums:
            if n%2 == cond:
                countEvenOdd += 1
                cond = not cond
                
        cond = 1
        countOddEven = 0
        for n in nums:
            if n%2 == cond:
                countOddEven += 1
                cond = not cond
        
        return max(countEven, countOdd, countEvenOdd, countOddEven)