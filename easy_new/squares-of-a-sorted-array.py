class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/squares-of-a-sorted-array/
        posSquared = []
        negSquared = []
        
        for num in nums:
            if num < 0:
                negSquared.append(num**2)
            else:
                posSquared.append(num**2)
        
        negSquared = negSquared[::-1]
        print(posSquared, negSquared)
        sol = []
        i, j = 0, 0
        for _ in range(len(nums)):
            if i >= len(posSquared):
                sol.append(negSquared[j])
                j += 1
            elif j >= len(negSquared):
                sol.append(posSquared[i])
                i += 1
            elif posSquared[i] <= negSquared[j]:
                sol.append(posSquared[i])
                i += 1
            else:
                sol.append(negSquared[j])
                j += 1
                
        return sol