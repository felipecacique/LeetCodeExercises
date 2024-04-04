class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

        # lets use pointers

        a = 0
        b = len(numbers) - 1
        while a < b:
            if numbers[a] + numbers[b] > target: # we need to deacrease our sum to reach target. Because it is in ordered, there is only one way that is moving b to the left, picking up a smaller number, which decrease the sum
                b-=1
            elif numbers[a] + numbers[b] < target:
                a+=1
            else: # numbers[a] + numbers[b] == target:
                return [a+1, b+1]
                
        return None