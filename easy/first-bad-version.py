# https://leetcode.com/problems/first-bad-version/submissions/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # we will do a binary search time O(log(n)) space O(1)

        start = 1
        end = n

        while start != end:
            middle = int((start + end) / 2)
            if isBadVersion(middle) == True:
                # solution is in middle or the left part
                end = middle
            else:
                # solution is in the right part
                start = middle + 1

        return start
