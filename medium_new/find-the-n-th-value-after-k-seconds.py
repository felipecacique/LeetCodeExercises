class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/description/
        # O(n^2) find the pattern in the examples
        arr = [1] * n
        for j in range(k):
            for i in range(1,n):
                arr[i] = arr[i-1] + arr[i]
        return arr[-1] % (10**9+7)