# too slow to pass the test cases
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # https://leetcode.com/problems/find-the-count-of-good-integers/description/
        import math
        good = set()

        def Permutations(nums):
            permutations = set()
            def helper(perm, visited):
                if len(perm) == len(nums):
                    permutations.add(tuple(perm))
                    return

                for i in range(len(nums)):
                    if not i in visited:
                        perm.append(i)
                        visited.add(i)
                        helper(perm, visited)
                        perm.pop()
                        visited.remove(i)
            helper([], set([]))

            return [ [nums[i] for i in permutation] for permutation in permutations ]
            

        def backtracking(num):
            if len(num) == math.ceil(n/2):
                if n % 2 == 1: candidate = num[:-1] + num[::-1] # odd, so we cannot replicate the last char, that will be in the middle od candidate
                else: candidate = num[:] + num[::-1] # even
                candidateInt = 0
                for i in range(len(candidate)): candidateInt += candidate[i] * 10**i
                if candidateInt % k == 0: 
                    # create a combination of all numbers of candidate
                    permutations = Permutations(candidate)
                    for permutation in permutations:
                        if permutation[0] == 0: continue # no leading zeroes
                        good.add(tuple(permutation))
                return 
         
            for i in range(0,10):
                num.append(i)
                if num[0] == 0: 
                    num.pop()
                    continue # no leading zeroes
                backtracking(num)
                num.pop()

        backtracking([])

        return len(good)