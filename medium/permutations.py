class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Solution1: Iterative with lists. We will do all permutations adding all numbers to the first position, leading to an set of partial solutions. For each partial solution, we add all nums in the second position, and so on untill we have all permutation. We need to avoid adding the same number to the solution more than 1 time. For that we will keep for each partial solution also a set() with the numbers of the solution. This way will be faster to check if the new number that we are about to add is already there or not. time(n^n)
        def Solution1(nums):
            n = len(nums)
            solutions_set = [ ([], set()) ]    
            
            for i in range(0, n): # will creat ethe solution of length == 1, length == 2 ...

                solutions_size_i = []

                for solution, solution_nums in solutions_set: # get the previous solution (e.g., length == 1) and add the next number
                    
                    for num in nums: # add all nums to the position i
                        if not num in solution_nums:
                            new_solution = solution.copy()
                            new_solution.append(num)
                            new_solution_nums = solution_nums.copy()
                            new_solution_nums.add(num)
                            solutions_size_i.append( (new_solution, new_solution_nums) )
                        
                solutions_set = solutions_size_i

            solutions = []
            for solution, solution_nums in solutions_set:
                solutions.append(solution)
            
            return solutions
        

        def Solution2(nums):
            # recursive
            pass

        return Solution1(nums)
