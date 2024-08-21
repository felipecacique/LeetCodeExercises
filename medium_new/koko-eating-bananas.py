class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # https://leetcode.com/problems/koko-eating-bananas/?envType=study-plan-v2&envId=leetcode-75
        # i got the solution from neetcode https://www.youtube.com/watch?v=U2SozAs9RzA
        # time (logm * n) where piles.max = m
        r = max(piles)
        l = 1
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res