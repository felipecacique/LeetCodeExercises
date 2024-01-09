# https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        # # Solution 1: we can create a binary tree, where the left has value 1 and right has value 2. A we will compute the sum of steps as we do a dfs. We stop creating the branches (stop in a leaf) when the sum > n. Now we just have to count the number of nodes. O(all combinations)

        # 1 1 1 1 1 1
        # lets supose n
        # if we link the fist 2 steps, we are left with n-2 remainig steps
        # if we do not link the firt 2 steps, we are left with n-1 remainig steps
        # these possibilities repeat until we have no steps left

        # remaining_steps = n

        # # Solution 2: what about doing something like divide and conquer
        # if we divide the stais in half, we have that the combinations are the left side combinations times the right side combinations, and taking attention to the join (last stair on the left (last_left) and the first stair of the right side (fisst_right)). If last_left is one step, ok. So the left and right sides are independent. If the last_left and the first_right belongs to a 2 steps, then, the left and right sides depends on each other.
        # Since we are dividing the problem, would make sense to do a recursive approach. Before that, how can this approach be better than the simple tree approach??

        # def Solution2(n):

        #     harsh = {}
        #     def climbStairs(n)

        #         if n == 1:
        #             return 1

        #         combinations = 1
        #         # independent situation (last_left is one step)
        #         # combinations_independent = comb(start,int((start+end))/2)) * comb(int((start+end))/2),right)
        #         combinations_independent = climbStairs(int(n/2)) * climbStairs(int(n/2))
        #         # both sides depends on each other (the last_left and the first_right belongs to a 2 steps)
        #         # combinations_dependent = comb(start,int((start+end))/2)-1) * comb(int((start+end))/2)+1,right)
        #         combinations_dependent = climbStairs(int(n/2)-1) * climbStairs(int(n/2)-1)

        #         return combinations_independent + combinations_dependent

        #     return climbStairs(n)

        # Solution 3: Similar to the soluition 3, but the idea is create the answer iteratively, bit by bit, using the previous solutions for n-1. Something like fibonatti. Solution of n is the solution of n-1 (in case the n-th is one step) + solution of n-2 (in case the n-th and the n-th-1 belogs to 2 step). Now we can use recursion and hash table (dynamic programming) to solve the problem afficiently like the fibonacci problem. Since we do not have to go through all combinantion paths such as we would do in the tree solution (solution 1):

        def Solution3(n):
            harsh = {}

            def climbStairs(n):
                if n in harsh:
                    return harsh[n]

                if n == 1:
                    return 1

                if n == 2:
                    return 2

                if n == 3:
                    return 3

                combinations = climbStairs(n - 1) + climbStairs(n - 2)

                harsh[n] = combinations

                return combinations

            return climbStairs(n)

        def Solution4(n):  # the same as Solution4, but a bit quicker
            harsh = {}

            def climbStairs(n):
                if n == 1:
                    return 1

                if n == 2:
                    return 2

                if n == 3:
                    return 3

                if n - 1 in harsh:
                    comb_n_1 = harsh[n - 1]
                else:
                    comb_n_1 = climbStairs(n - 1)

                if n - 2 in harsh:
                    comb_n_2 = harsh[n - 2]
                else:
                    comb_n_2 = climbStairs(n - 2)

                combinations = comb_n_1 + comb_n_2

                harsh[n] = combinations

                return combinations

            return climbStairs(n)

        return Solution4(n)
