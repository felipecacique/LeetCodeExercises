class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150
        
        def Solution1(): # O(n^k)
            combs = [[]]
            for i in range(k):
                new_combs = []
                for comb in combs:
                    start = comb[-1] + 1 if comb else 1
                    for j in range(start,n+1):
                        new_comb = comb + [j]
                        new_combs.append(new_comb)
                combs = new_combs
            return combs

        def Solution2(): # backtracking, traverse in order
            combs = []
            def backtrack(comb,k):
                if k == 0:
                    combs.append(comb)
                    return
                start = comb[-1] + 1 if comb else 1
                for j in range(start,n+1):
                    backtrack(comb+[j], k-1)
            backtrack([],k)
            return combs

        return Solution2()


