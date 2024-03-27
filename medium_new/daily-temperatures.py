class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # https://leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75
        # problem of finding the next greatter element, using monotonic stack O(n)
        # solve like next-greater-element-i problem, but stores the indexes. Then we subtract it to know the number of days

        stack = []
        solution = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):

            while stack and stack[-1][0] < temperature: 
                # we will pop temperatures here
                temp, j = stack.pop() # temp is popped by temperature, so temperature is the temp nest greatest temperature, and the days passed is i - j
                days = i - j
                solution[j] = days

            stack.append((temperature, i))

        return solution
            
