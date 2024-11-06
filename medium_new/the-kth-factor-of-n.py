class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # https://leetcode.com/problems/the-kth-factor-of-n/submissions/1445172336/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
        ans = []
        for num in range(1,n+1):
            if n % num == 0:
                ans.append(num)
                if len(ans) == k:
                    return ans[-1]
        return -1