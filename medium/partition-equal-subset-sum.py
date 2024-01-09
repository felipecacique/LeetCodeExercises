# https://leetcode.com/problems/partition-equal-subset-sum/submissions/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # solution similar to combination-sum problem. Get the total sum. Each side must have half of the total sum. If we can aggregate the first half, the second half will definely be a subset with sum equal to the first half. The problem can change to: is there a subset of nums that has sum equal to n? We could also sort the array, or do a tree with memoization...  What we will do is adding num by num and keeping an set with all sums untill that point. We will build it up our solution from the buttom-up, having the option to add the num to the previous partial sums or not. It is similar to the  exercice combination-sum where we held all partial combinations, but in this case we only need to hold the partial sums. We use set() instead of list to avoid duplicates and redundant work.
        
        totalSum = sum(nums)
        
        if totalSum % 2 == 1:   # odd number
            return False
        
        halfSum = totalSum / 2

        # lets find a subset where the sum in equal to halfSum
        # we will build the solution, adding number by number until sum = halfSum

        sums = set()
        sums.add(0)

        for num in nums: # get number umne by one
            
            sums_list = list(sums)
            for i in range(0, len(sums_list)): # for each sum, we can add the number to the sum or not, making new solutions. We will build "all" de solutions without having to hold the combinations of nums, only the sum
                new_sum = sums_list[i]+num
                if new_sum == halfSum:  # there is a subset with sum equal to halfSum
                    return True
                sums.add(new_sum)
        
        return False
            


