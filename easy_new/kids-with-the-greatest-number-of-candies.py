class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
        
        maxNumber = max(candies)
        solution = []

        for i in range(0,len(candies)):
            solution.append( True if candies[i] + extraCandies >= maxNumber else False )
        
        return solution