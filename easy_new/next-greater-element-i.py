class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # https://leetcode.com/problems/next-greater-element-i/
        # using monotonic stack (stack that mantains a certain property) which is useful in solving problems where we need to find the next greatter element 

        stack = []
        next_greater = {}
        solution = []

        for num in nums2:
            # add the num to the stack, it must pop the values smaller than him
            while stack and stack[-1] <= num:
                n = stack.pop() # n is popped by the num, so num is the n next greater number 
                next_greater[n] = num
            stack.append(num)

        # look up each element in num1 in the dictionary
        for num in nums1:
            solution.append(next_greater.get(num,-1))
        
        return solution