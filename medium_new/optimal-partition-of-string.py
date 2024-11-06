class Solution:
    def partitionString(self, s: str) -> int:
        # https://leetcode.com/problems/optimal-partition-of-string/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
        # we can go greedy O(n)
        chars = set()
        ans = 1
        for c in s:
            if c in chars: # create a new group
                chars = set()
                ans += 1
            chars.add(c)
        return ans
