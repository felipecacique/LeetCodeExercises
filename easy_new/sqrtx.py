class Solution:
    def mySqrt(self, x: int) -> int:
        # https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150
        start = 0
        end = x
        while start <= end:
            middle = (start+end) // 2
            if middle * middle == x:
                return middle
            elif middle * middle < x:
                start = middle + 1
            else:
                end = middle - 1
        return end        
        